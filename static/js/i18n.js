/**
 * SeniorCare - Sistema de Internacionalização (i18n)
 * Suporta múltiplos idiomas com deteção automática
 */

const i18n = {
    // Idioma atual
    currentLang: 'pt',
    
    // Idiomas suportados
    supportedLanguages: {
        'pt': { name: 'Português', flag: '🇵🇹', dir: 'ltr' },
        'en': { name: 'English', flag: '🇬🇧', dir: 'ltr' },
        'es': { name: 'Español', flag: '🇪🇸', dir: 'ltr' },
        'fr': { name: 'Français', flag: '🇫🇷', dir: 'ltr' },
        'de': { name: 'Deutsch', flag: '🇩🇪', dir: 'ltr' },
        'it': { name: 'Italiano', flag: '🇮🇹', dir: 'ltr' },
    },
    
    // Traduções
    translations: {
        // ==================== PORTUGUÊS ====================
        'pt': {
            // Geral
            app_name: 'SeniorCare',
            loading: 'A carregar...',
            back: 'Voltar',
            cancel: 'Cancelar',
            save: 'Guardar',
            confirm: 'Confirmar',
            yes: 'Sim',
            no: 'Não',
            ok: 'OK',
            error: 'Erro',
            success: 'Sucesso',
            settings: 'Definições',
            
            // Saudações
            greeting_morning: 'Bom dia',
            greeting_afternoon: 'Boa tarde',
            greeting_evening: 'Boa noite',
            
            // Ecrã principal
            home_companion: 'Conversar',
            home_medication: 'Medicação',
            home_family: 'Família',
            home_routine: 'Rotina',
            home_status_ok: 'Está tudo bem consigo!',
            home_status_check: 'Última verificação há pouco',
            next_reminder: 'Próximo lembrete',
            
            // Medicação
            medication_title: 'Medicação de Hoje',
            medication_pending: 'Por tomar',
            medication_taken: 'Já tomados',
            medication_take_btn: 'Tomei',
            medication_all_taken: 'Parabéns!',
            medication_all_taken_msg: 'Tomou toda a medicação de hoje',
            medication_at: 'às',
            
            // Família
            family_title: 'Família',
            family_calling: 'A ligar...',
            family_call: 'Ligar',
            
            // Conversa
            companion_title: 'Conversar',
            companion_listening: 'A ouvir... Toque para parar',
            companion_tap_speak: 'Tocar para falar',
            companion_greeting: 'Olá! Como se sente hoje? Estou aqui para conversar consigo. 😊',
            
            // Respostas rápidas
            quick_feeling_good: 'Estou bem, obrigado!',
            quick_tell_story: 'Conte-me uma história',
            quick_what_day: 'Que dia é hoje?',
            quick_play_music: 'Quero ouvir música',
            
            // Rotina
            routine_title: 'A Minha Rotina',
            
            // Emergência
            emergency_title: 'Emergência',
            emergency_question: 'Precisa de ajuda urgente?',
            emergency_call_112: 'Ligar 112',
            emergency_alert_family: 'Alertar Família',
            emergency_calling: 'A ligar para o 112...',
            emergency_alerting: 'A notificar a família...',
            
            // Definições
            settings_title: 'Definições',
            settings_language: 'Idioma',
            settings_language_desc: 'Escolha o idioma da aplicação',
            settings_profile: 'Perfil',
            settings_notifications: 'Notificações',
            settings_about: 'Sobre',
            settings_version: 'Versão',
            
            // Relações familiares
            relation_daughter: 'Filha',
            relation_son: 'Filho',
            relation_granddaughter: 'Neta',
            relation_grandson: 'Neto',
            relation_wife: 'Esposa',
            relation_husband: 'Marido',
            relation_doctor: 'Médico',
            relation_nurse: 'Enfermeiro(a)',
            relation_caregiver: 'Cuidador(a)',
            
            // Atividades
            activity_walk: 'Caminhada matinal',
            activity_medication: 'Tomar medicação',
            activity_breakfast: 'Pequeno-almoço',
            activity_lunch: 'Almoço',
            activity_dinner: 'Jantar',
            activity_rest: 'Descanso',
            activity_exercise: 'Exercícios leves',
            activity_call: 'Telefonar',
            
            // Desktop warning
            desktop_warning_title: 'SeniorCare é uma app mobile',
            desktop_warning_msg: 'Esta aplicação foi desenhada para ser usada em smartphones e tablets. Por favor, aceda através do seu dispositivo móvel para a melhor experiência.',
            desktop_test_mode: 'Entrar em modo de teste (Desktop)',
            
            // Erros
            error_connection: 'Erro de ligação',
            error_try_again: 'Tente novamente',
        },
        
        // ==================== ENGLISH ====================
        'en': {
            // General
            app_name: 'SeniorCare',
            loading: 'Loading...',
            back: 'Back',
            cancel: 'Cancel',
            save: 'Save',
            confirm: 'Confirm',
            yes: 'Yes',
            no: 'No',
            ok: 'OK',
            error: 'Error',
            success: 'Success',
            settings: 'Settings',
            
            // Greetings
            greeting_morning: 'Good morning',
            greeting_afternoon: 'Good afternoon',
            greeting_evening: 'Good evening',
            
            // Home screen
            home_companion: 'Chat',
            home_medication: 'Medication',
            home_family: 'Family',
            home_routine: 'Routine',
            home_status_ok: 'Everything is fine!',
            home_status_check: 'Last check a moment ago',
            next_reminder: 'Next reminder',
            
            // Medication
            medication_title: "Today's Medication",
            medication_pending: 'Pending',
            medication_taken: 'Already taken',
            medication_take_btn: 'Taken',
            medication_all_taken: 'Congratulations!',
            medication_all_taken_msg: "You've taken all medication for today",
            medication_at: 'at',
            
            // Family
            family_title: 'Family',
            family_calling: 'Calling...',
            family_call: 'Call',
            
            // Companion
            companion_title: 'Chat',
            companion_listening: 'Listening... Tap to stop',
            companion_tap_speak: 'Tap to speak',
            companion_greeting: "Hello! How are you feeling today? I'm here to chat with you. 😊",
            
            // Quick replies
            quick_feeling_good: "I'm fine, thank you!",
            quick_tell_story: 'Tell me a story',
            quick_what_day: 'What day is it?',
            quick_play_music: 'I want to hear music',
            
            // Routine
            routine_title: 'My Routine',
            
            // Emergency
            emergency_title: 'Emergency',
            emergency_question: 'Do you need urgent help?',
            emergency_call_112: 'Call 112',
            emergency_alert_family: 'Alert Family',
            emergency_calling: 'Calling 112...',
            emergency_alerting: 'Notifying family...',
            
            // Settings
            settings_title: 'Settings',
            settings_language: 'Language',
            settings_language_desc: 'Choose the app language',
            settings_profile: 'Profile',
            settings_notifications: 'Notifications',
            settings_about: 'About',
            settings_version: 'Version',
            
            // Family relations
            relation_daughter: 'Daughter',
            relation_son: 'Son',
            relation_granddaughter: 'Granddaughter',
            relation_grandson: 'Grandson',
            relation_wife: 'Wife',
            relation_husband: 'Husband',
            relation_doctor: 'Doctor',
            relation_nurse: 'Nurse',
            relation_caregiver: 'Caregiver',
            
            // Activities
            activity_walk: 'Morning walk',
            activity_medication: 'Take medication',
            activity_breakfast: 'Breakfast',
            activity_lunch: 'Lunch',
            activity_dinner: 'Dinner',
            activity_rest: 'Rest',
            activity_exercise: 'Light exercise',
            activity_call: 'Phone call',
            
            // Desktop warning
            desktop_warning_title: 'SeniorCare is a mobile app',
            desktop_warning_msg: 'This application was designed for smartphones and tablets. Please access from your mobile device for the best experience.',
            desktop_test_mode: 'Enter test mode (Desktop)',
            
            // Errors
            error_connection: 'Connection error',
            error_try_again: 'Try again',
        },
        
        // ==================== ESPAÑOL ====================
        'es': {
            // General
            app_name: 'SeniorCare',
            loading: 'Cargando...',
            back: 'Volver',
            cancel: 'Cancelar',
            save: 'Guardar',
            confirm: 'Confirmar',
            yes: 'Sí',
            no: 'No',
            ok: 'OK',
            error: 'Error',
            success: 'Éxito',
            settings: 'Ajustes',
            
            // Greetings
            greeting_morning: 'Buenos días',
            greeting_afternoon: 'Buenas tardes',
            greeting_evening: 'Buenas noches',
            
            // Home screen
            home_companion: 'Conversar',
            home_medication: 'Medicación',
            home_family: 'Familia',
            home_routine: 'Rutina',
            home_status_ok: '¡Todo está bien!',
            home_status_check: 'Última comprobación hace un momento',
            next_reminder: 'Próximo recordatorio',
            
            // Medication
            medication_title: 'Medicación de Hoy',
            medication_pending: 'Pendiente',
            medication_taken: 'Ya tomados',
            medication_take_btn: 'Tomado',
            medication_all_taken: '¡Felicidades!',
            medication_all_taken_msg: 'Ha tomado toda la medicación de hoy',
            medication_at: 'a las',
            
            // Family
            family_title: 'Familia',
            family_calling: 'Llamando...',
            family_call: 'Llamar',
            
            // Companion
            companion_title: 'Conversar',
            companion_listening: 'Escuchando... Toque para parar',
            companion_tap_speak: 'Tocar para hablar',
            companion_greeting: '¡Hola! ¿Cómo se siente hoy? Estoy aquí para conversar. 😊',
            
            // Quick replies
            quick_feeling_good: '¡Estoy bien, gracias!',
            quick_tell_story: 'Cuénteme una historia',
            quick_what_day: '¿Qué día es hoy?',
            quick_play_music: 'Quiero escuchar música',
            
            // Routine
            routine_title: 'Mi Rutina',
            
            // Emergency
            emergency_title: 'Emergencia',
            emergency_question: '¿Necesita ayuda urgente?',
            emergency_call_112: 'Llamar 112',
            emergency_alert_family: 'Alertar Familia',
            emergency_calling: 'Llamando al 112...',
            emergency_alerting: 'Notificando a la familia...',
            
            // Settings
            settings_title: 'Ajustes',
            settings_language: 'Idioma',
            settings_language_desc: 'Elija el idioma de la aplicación',
            settings_profile: 'Perfil',
            settings_notifications: 'Notificaciones',
            settings_about: 'Acerca de',
            settings_version: 'Versión',
            
            // Family relations
            relation_daughter: 'Hija',
            relation_son: 'Hijo',
            relation_granddaughter: 'Nieta',
            relation_grandson: 'Nieto',
            relation_wife: 'Esposa',
            relation_husband: 'Marido',
            relation_doctor: 'Médico',
            relation_nurse: 'Enfermero(a)',
            relation_caregiver: 'Cuidador(a)',
            
            // Activities
            activity_walk: 'Paseo matinal',
            activity_medication: 'Tomar medicación',
            activity_breakfast: 'Desayuno',
            activity_lunch: 'Almuerzo',
            activity_dinner: 'Cena',
            activity_rest: 'Descanso',
            activity_exercise: 'Ejercicios suaves',
            activity_call: 'Llamar',
            
            // Desktop warning
            desktop_warning_title: 'SeniorCare es una app móvil',
            desktop_warning_msg: 'Esta aplicación fue diseñada para smartphones y tablets. Por favor, acceda desde su dispositivo móvil.',
            desktop_test_mode: 'Entrar en modo prueba (Desktop)',
            
            // Errors
            error_connection: 'Error de conexión',
            error_try_again: 'Inténtelo de nuevo',
        },
        
        // ==================== FRANÇAIS ====================
        'fr': {
            // General
            app_name: 'SeniorCare',
            loading: 'Chargement...',
            back: 'Retour',
            cancel: 'Annuler',
            save: 'Enregistrer',
            confirm: 'Confirmer',
            yes: 'Oui',
            no: 'Non',
            ok: 'OK',
            error: 'Erreur',
            success: 'Succès',
            settings: 'Paramètres',
            
            // Greetings
            greeting_morning: 'Bonjour',
            greeting_afternoon: 'Bon après-midi',
            greeting_evening: 'Bonsoir',
            
            // Home screen
            home_companion: 'Discuter',
            home_medication: 'Médicaments',
            home_family: 'Famille',
            home_routine: 'Routine',
            home_status_ok: 'Tout va bien !',
            home_status_check: 'Dernière vérification il y a un instant',
            next_reminder: 'Prochain rappel',
            
            // Medication
            medication_title: "Médicaments d'Aujourd'hui",
            medication_pending: 'À prendre',
            medication_taken: 'Déjà pris',
            medication_take_btn: 'Pris',
            medication_all_taken: 'Félicitations !',
            medication_all_taken_msg: "Vous avez pris tous vos médicaments aujourd'hui",
            medication_at: 'à',
            
            // Family
            family_title: 'Famille',
            family_calling: 'Appel en cours...',
            family_call: 'Appeler',
            
            // Companion
            companion_title: 'Discuter',
            companion_listening: "J'écoute... Touchez pour arrêter",
            companion_tap_speak: 'Touchez pour parler',
            companion_greeting: 'Bonjour ! Comment vous sentez-vous ? Je suis là pour discuter. 😊',
            
            // Quick replies
            quick_feeling_good: 'Je vais bien, merci !',
            quick_tell_story: 'Racontez-moi une histoire',
            quick_what_day: 'Quel jour sommes-nous ?',
            quick_play_music: 'Je veux écouter de la musique',
            
            // Routine
            routine_title: 'Ma Routine',
            
            // Emergency
            emergency_title: 'Urgence',
            emergency_question: "Avez-vous besoin d'aide urgente ?",
            emergency_call_112: 'Appeler le 112',
            emergency_alert_family: 'Alerter la Famille',
            emergency_calling: 'Appel du 112...',
            emergency_alerting: 'Notification de la famille...',
            
            // Settings
            settings_title: 'Paramètres',
            settings_language: 'Langue',
            settings_language_desc: "Choisissez la langue de l'application",
            settings_profile: 'Profil',
            settings_notifications: 'Notifications',
            settings_about: 'À propos',
            settings_version: 'Version',
            
            // Family relations
            relation_daughter: 'Fille',
            relation_son: 'Fils',
            relation_granddaughter: 'Petite-fille',
            relation_grandson: 'Petit-fils',
            relation_wife: 'Épouse',
            relation_husband: 'Mari',
            relation_doctor: 'Médecin',
            relation_nurse: 'Infirmier(ère)',
            relation_caregiver: 'Soignant(e)',
            
            // Activities
            activity_walk: 'Promenade matinale',
            activity_medication: 'Prendre les médicaments',
            activity_breakfast: 'Petit-déjeuner',
            activity_lunch: 'Déjeuner',
            activity_dinner: 'Dîner',
            activity_rest: 'Repos',
            activity_exercise: 'Exercices légers',
            activity_call: 'Appeler',
            
            // Desktop warning
            desktop_warning_title: 'SeniorCare est une app mobile',
            desktop_warning_msg: 'Cette application est conçue pour smartphones et tablettes. Veuillez y accéder depuis votre appareil mobile.',
            desktop_test_mode: 'Mode test (Bureau)',
            
            // Errors
            error_connection: 'Erreur de connexion',
            error_try_again: 'Réessayez',
        },
        
        // ==================== DEUTSCH ====================
        'de': {
            // General
            app_name: 'SeniorCare',
            loading: 'Laden...',
            back: 'Zurück',
            cancel: 'Abbrechen',
            save: 'Speichern',
            confirm: 'Bestätigen',
            yes: 'Ja',
            no: 'Nein',
            ok: 'OK',
            error: 'Fehler',
            success: 'Erfolg',
            settings: 'Einstellungen',
            
            // Greetings
            greeting_morning: 'Guten Morgen',
            greeting_afternoon: 'Guten Tag',
            greeting_evening: 'Guten Abend',
            
            // Home screen
            home_companion: 'Plaudern',
            home_medication: 'Medikamente',
            home_family: 'Familie',
            home_routine: 'Tagesablauf',
            home_status_ok: 'Alles ist in Ordnung!',
            home_status_check: 'Letzte Überprüfung vor kurzem',
            next_reminder: 'Nächste Erinnerung',
            
            // Medication
            medication_title: 'Heutige Medikamente',
            medication_pending: 'Ausstehend',
            medication_taken: 'Bereits genommen',
            medication_take_btn: 'Genommen',
            medication_all_taken: 'Herzlichen Glückwunsch!',
            medication_all_taken_msg: 'Sie haben heute alle Medikamente genommen',
            medication_at: 'um',
            
            // Family
            family_title: 'Familie',
            family_calling: 'Anruf läuft...',
            family_call: 'Anrufen',
            
            // Companion
            companion_title: 'Plaudern',
            companion_listening: 'Ich höre... Tippen zum Stoppen',
            companion_tap_speak: 'Tippen zum Sprechen',
            companion_greeting: 'Hallo! Wie fühlen Sie sich heute? Ich bin hier zum Plaudern. 😊',
            
            // Quick replies
            quick_feeling_good: 'Mir geht es gut, danke!',
            quick_tell_story: 'Erzählen Sie mir eine Geschichte',
            quick_what_day: 'Welcher Tag ist heute?',
            quick_play_music: 'Ich möchte Musik hören',
            
            // Routine
            routine_title: 'Mein Tagesablauf',
            
            // Emergency
            emergency_title: 'Notfall',
            emergency_question: 'Brauchen Sie dringend Hilfe?',
            emergency_call_112: '112 anrufen',
            emergency_alert_family: 'Familie alarmieren',
            emergency_calling: 'Rufe 112 an...',
            emergency_alerting: 'Familie wird benachrichtigt...',
            
            // Settings
            settings_title: 'Einstellungen',
            settings_language: 'Sprache',
            settings_language_desc: 'Wählen Sie die App-Sprache',
            settings_profile: 'Profil',
            settings_notifications: 'Benachrichtigungen',
            settings_about: 'Über',
            settings_version: 'Version',
            
            // Family relations
            relation_daughter: 'Tochter',
            relation_son: 'Sohn',
            relation_granddaughter: 'Enkelin',
            relation_grandson: 'Enkel',
            relation_wife: 'Ehefrau',
            relation_husband: 'Ehemann',
            relation_doctor: 'Arzt',
            relation_nurse: 'Krankenschwester',
            relation_caregiver: 'Betreuer(in)',
            
            // Activities
            activity_walk: 'Morgenspaziergang',
            activity_medication: 'Medikamente nehmen',
            activity_breakfast: 'Frühstück',
            activity_lunch: 'Mittagessen',
            activity_dinner: 'Abendessen',
            activity_rest: 'Ruhe',
            activity_exercise: 'Leichte Übungen',
            activity_call: 'Anrufen',
            
            // Desktop warning
            desktop_warning_title: 'SeniorCare ist eine mobile App',
            desktop_warning_msg: 'Diese Anwendung wurde für Smartphones und Tablets entwickelt. Bitte greifen Sie von Ihrem Mobilgerät aus zu.',
            desktop_test_mode: 'Testmodus (Desktop)',
            
            // Errors
            error_connection: 'Verbindungsfehler',
            error_try_again: 'Erneut versuchen',
        },
        
        // ==================== ITALIANO ====================
        'it': {
            // General
            app_name: 'SeniorCare',
            loading: 'Caricamento...',
            back: 'Indietro',
            cancel: 'Annulla',
            save: 'Salva',
            confirm: 'Conferma',
            yes: 'Sì',
            no: 'No',
            ok: 'OK',
            error: 'Errore',
            success: 'Successo',
            settings: 'Impostazioni',
            
            // Greetings
            greeting_morning: 'Buongiorno',
            greeting_afternoon: 'Buon pomeriggio',
            greeting_evening: 'Buonasera',
            
            // Home screen
            home_companion: 'Chiacchierare',
            home_medication: 'Medicinali',
            home_family: 'Famiglia',
            home_routine: 'Routine',
            home_status_ok: 'Tutto bene!',
            home_status_check: 'Ultimo controllo poco fa',
            next_reminder: 'Prossimo promemoria',
            
            // Medication
            medication_title: 'Medicinali di Oggi',
            medication_pending: 'Da prendere',
            medication_taken: 'Già presi',
            medication_take_btn: 'Preso',
            medication_all_taken: 'Complimenti!',
            medication_all_taken_msg: 'Hai preso tutti i medicinali di oggi',
            medication_at: 'alle',
            
            // Family
            family_title: 'Famiglia',
            family_calling: 'Chiamata in corso...',
            family_call: 'Chiama',
            
            // Companion
            companion_title: 'Chiacchierare',
            companion_listening: 'Ascolto... Tocca per fermare',
            companion_tap_speak: 'Tocca per parlare',
            companion_greeting: 'Ciao! Come si sente oggi? Sono qui per chiacchierare. 😊',
            
            // Quick replies
            quick_feeling_good: 'Sto bene, grazie!',
            quick_tell_story: 'Raccontami una storia',
            quick_what_day: 'Che giorno è oggi?',
            quick_play_music: 'Voglio ascoltare musica',
            
            // Routine
            routine_title: 'La Mia Routine',
            
            // Emergency
            emergency_title: 'Emergenza',
            emergency_question: 'Ha bisogno di aiuto urgente?',
            emergency_call_112: 'Chiama 112',
            emergency_alert_family: 'Avvisa Famiglia',
            emergency_calling: 'Chiamando il 112...',
            emergency_alerting: 'Avviso alla famiglia...',
            
            // Settings
            settings_title: 'Impostazioni',
            settings_language: 'Lingua',
            settings_language_desc: "Scegli la lingua dell'app",
            settings_profile: 'Profilo',
            settings_notifications: 'Notifiche',
            settings_about: 'Info',
            settings_version: 'Versione',
            
            // Family relations
            relation_daughter: 'Figlia',
            relation_son: 'Figlio',
            relation_granddaughter: 'Nipote',
            relation_grandson: 'Nipote',
            relation_wife: 'Moglie',
            relation_husband: 'Marito',
            relation_doctor: 'Medico',
            relation_nurse: 'Infermiere/a',
            relation_caregiver: 'Badante',
            
            // Activities
            activity_walk: 'Passeggiata mattutina',
            activity_medication: 'Prendere medicinali',
            activity_breakfast: 'Colazione',
            activity_lunch: 'Pranzo',
            activity_dinner: 'Cena',
            activity_rest: 'Riposo',
            activity_exercise: 'Esercizi leggeri',
            activity_call: 'Telefonare',
            
            // Desktop warning
            desktop_warning_title: "SeniorCare è un'app mobile",
            desktop_warning_msg: "Questa applicazione è progettata per smartphone e tablet. Accedi dal tuo dispositivo mobile.",
            desktop_test_mode: 'Modalità test (Desktop)',
            
            // Errors
            error_connection: 'Errore di connessione',
            error_try_again: 'Riprova',
        },
    },
    
    /**
     * Inicializar o sistema i18n
     */
    init() {
        // Tentar carregar idioma guardado
        const savedLang = localStorage.getItem('seniorcare_language');
        if (savedLang && this.supportedLanguages[savedLang]) {
            this.currentLang = savedLang;
        } else {
            // Detetar idioma do browser
            const browserLang = navigator.language.split('-')[0];
            if (this.supportedLanguages[browserLang]) {
                this.currentLang = browserLang;
            }
        }
        
        // Aplicar direção do texto (para idiomas RTL no futuro)
        document.documentElement.dir = this.supportedLanguages[this.currentLang].dir;
        document.documentElement.lang = this.currentLang;
        
        console.log(`i18n: Idioma inicializado - ${this.currentLang}`);
    },
    
    /**
     * Obter tradução
     * @param {string} key - Chave da tradução
     * @param {object} params - Parâmetros para substituição
     * @returns {string} Texto traduzido
     */
    t(key, params = {}) {
        let text = this.translations[this.currentLang]?.[key] 
                || this.translations['en']?.[key] 
                || key;
        
        // Substituir parâmetros {{param}}
        Object.keys(params).forEach(param => {
            text = text.replace(new RegExp(`{{${param}}}`, 'g'), params[param]);
        });
        
        return text;
    },
    
    /**
     * Mudar idioma
     * @param {string} lang - Código do idioma
     */
    setLanguage(lang) {
        if (this.supportedLanguages[lang]) {
            this.currentLang = lang;
            localStorage.setItem('seniorcare_language', lang);
            document.documentElement.dir = this.supportedLanguages[lang].dir;
            document.documentElement.lang = lang;
            
            // Disparar evento para atualizar UI
            window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
            
            console.log(`i18n: Idioma alterado para ${lang}`);
            return true;
        }
        return false;
    },
    
    /**
     * Obter idioma atual
     * @returns {string} Código do idioma
     */
    getLanguage() {
        return this.currentLang;
    },
    
    /**
     * Obter lista de idiomas suportados
     * @returns {object} Idiomas suportados
     */
    getLanguages() {
        return this.supportedLanguages;
    },
    
    /**
     * Obter saudação baseada na hora
     * @returns {string} Saudação traduzida
     */
    getGreeting() {
        const hour = new Date().getHours();
        if (hour < 12) return this.t('greeting_morning');
        if (hour < 19) return this.t('greeting_afternoon');
        return this.t('greeting_evening');
    }
};

// Atalho global para tradução
const t = (key, params) => i18n.t(key, params);

// Inicializar quando o DOM carregar
if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => i18n.init());
}

// Exportar para uso em módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { i18n, t };
}
