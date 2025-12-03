// SeniorCare - Service Worker
const CACHE_NAME = 'seniorcare-v1';
const OFFLINE_URL = '/';

const ASSETS_TO_CACHE = [
    '/',
    '/manifest.json',
    '/static/icons/icon-192.png',
    '/static/icons/icon-512.png',
    'https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap'
];

// Instalação - cache de assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            console.log('SeniorCare: Caching assets');
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
    self.skipWaiting();
});

// Ativação - limpar caches antigos
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('SeniorCare: Removing old cache', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

// Fetch - estratégia network-first para API, cache-first para assets
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);

    // API calls - network first
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(
            fetch(request)
                .then((response) => {
                    // Cache successful GET requests
                    if (request.method === 'GET' && response.status === 200) {
                        const responseClone = response.clone();
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(request, responseClone);
                        });
                    }
                    return response;
                })
                .catch(() => {
                    // Return cached version if offline
                    return caches.match(request);
                })
        );
        return;
    }

    // Static assets - cache first
    event.respondWith(
        caches.match(request).then((cachedResponse) => {
            if (cachedResponse) {
                // Update cache in background
                fetch(request).then((response) => {
                    if (response.status === 200) {
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(request, response);
                        });
                    }
                }).catch(() => {});
                return cachedResponse;
            }

            return fetch(request).then((response) => {
                if (response.status === 200) {
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(request, responseClone);
                    });
                }
                return response;
            }).catch(() => {
                // Return offline page for navigation requests
                if (request.mode === 'navigate') {
                    return caches.match(OFFLINE_URL);
                }
            });
        })
    );
});

// Push notifications
self.addEventListener('push', (event) => {
    const options = {
        body: event.data ? event.data.text() : 'Nova notificação',
        icon: '/static/icons/icon-192.png',
        badge: '/static/icons/icon-72.png',
        vibrate: [200, 100, 200],
        tag: 'seniorcare-notification',
        requireInteraction: true,
        actions: [
            { action: 'open', title: 'Abrir' },
            { action: 'dismiss', title: 'Fechar' }
        ]
    };

    event.waitUntil(
        self.registration.showNotification('SeniorCare', options)
    );
});

// Notification click
self.addEventListener('notificationclick', (event) => {
    event.notification.close();

    if (event.action === 'open' || !event.action) {
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});

// Background sync for offline actions
self.addEventListener('sync', (event) => {
    if (event.tag === 'sync-medications') {
        event.waitUntil(syncMedications());
    }
    if (event.tag === 'sync-alerts') {
        event.waitUntil(syncAlerts());
    }
});

async function syncMedications() {
    // Sync pending medication logs when online
    const cache = await caches.open(CACHE_NAME);
    const pendingLogs = await cache.match('pending-medication-logs');
    
    if (pendingLogs) {
        const logs = await pendingLogs.json();
        for (const log of logs) {
            try {
                await fetch('/api/medications/' + log.medicationId + '/take', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(log)
                });
            } catch (error) {
                console.error('Failed to sync medication log:', error);
            }
        }
        await cache.delete('pending-medication-logs');
    }
}

async function syncAlerts() {
    // Sync pending alerts when online
    const cache = await caches.open(CACHE_NAME);
    const pendingAlerts = await cache.match('pending-alerts');
    
    if (pendingAlerts) {
        const alerts = await pendingAlerts.json();
        for (const alert of alerts) {
            try {
                await fetch('/api/alerts/emergency', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(alert)
                });
            } catch (error) {
                console.error('Failed to sync alert:', error);
            }
        }
        await cache.delete('pending-alerts');
    }
}

console.log('SeniorCare Service Worker loaded');
