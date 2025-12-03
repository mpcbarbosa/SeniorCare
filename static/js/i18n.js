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
            add: 'Adicionar',
            edit: 'Editar',
            delete: 'Apagar',
            undo: 'Desfazer',
            
            // Saudações
            greeting_morning: 'Bom dia',
            greeting_afternoon: 'Boa tarde',
            greeting_evening: 'Boa noite',
            
            // Ecrã principal
            home_companion: 'Conversar',
            home_medication: 'Medicação',
            home_family: 'Família',
            home_routine: 'Rotina',
            home_appointments: 'Consultas',
            home_health: 'Saúde',
            home_status_ok: 'Está tudo bem consigo!',
            home_status_check: 'Última verificação há pouco',
            next_reminder: 'Próximo lembrete',
            
            // Medicação
            medication_title: 'Medicação de Hoje',
            medication_pending: 'Por tomar',
            medication_taken: 'Já tomados',
            medication_take_btn: 'Tomei',
            medication_undo_btn: 'Não tomei',
            medication_all_taken: 'Parabéns!',
            medication_all_taken_msg: 'Tomou toda a medicação de hoje',
            medication_at: 'às',
            medication_missed: 'Medicação em atraso',
            medication_missed_msg: 'Está na hora de tomar',
            
            // Consultas
            appointments_title: 'Consultas',
            appointments_upcoming: 'Próximas consultas',
            appointments_past: 'Consultas anteriores',
            appointments_add: 'Marcar consulta',
            appointments_none: 'Sem consultas marcadas',
            appointments_doctor: 'Médico/Especialidade',
            appointments_date: 'Data',
            appointments_time: 'Hora',
            appointments_location: 'Local',
            appointments_notes: 'Notas',
            appointments_done: 'Realizada',
            appointments_mark_done: 'Marcar como realizada',
            
            // Registos de Saúde
            health_title: 'Registos de Saúde',
            health_add: 'Novo registo',
            health_blood_pressure: 'Tensão Arterial',
            health_blood_pressure_sys: 'Sistólica (máx)',
            health_blood_pressure_dia: 'Diastólica (mín)',
            health_heart_rate: 'Batimentos',
            health_glucose: 'Glicemia',
            health_weight: 'Peso',
            health_temperature: 'Temperatura',
            health_oxygen: 'Oxigénio no Sangue',
            health_unit_mmhg: 'mmHg',
            health_unit_bpm: 'bpm',
            health_unit_mgdl: 'mg/dL',
            health_unit_kg: 'kg',
            health_unit_celsius: '°C',
            health_unit_percent: '%',
            health_history: 'Histórico',
            health_no_records: 'Sem registos',
            health_last_record: 'Último registo',
            
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
            settings_notifications: 'Notificações',
            settings_notifications_desc: 'Configurar alertas para a família',
            settings_notify_all: 'Todas as notificações',
            settings_notify_medication: 'Só falhas de medicação',
            settings_notify_emergency: 'Só emergências',
            settings_notify_none: 'Nenhuma',
            settings_notify_family_label: 'Alertar família quando:',
            settings_profile: 'Perfil',
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
            error_fill_fields: 'Preencha os campos obrigatórios',
            
            // Sucesso
            success_saved: 'Guardado com sucesso',
            success_recorded: 'Registado com sucesso',
            
            // Consultas
            appointments_title: 'Consultas',
            appointments_upcoming: 'Próximas Consultas',
            appointments_past: 'Consultas Anteriores',
            appointments_add: 'Agendar Consulta',
            appointments_no_upcoming: 'Sem consultas agendadas',
            appointments_doctor: 'Médico',
            appointments_specialty: 'Especialidade',
            appointments_location: 'Local',
            appointments_date: 'Data',
            appointments_time: 'Hora',
            appointments_notes: 'Notas',
            appointments_reminder: 'Lembrete',
            appointments_hours_before: 'horas antes',
            appointments_status_scheduled: 'Agendada',
            appointments_status_completed: 'Realizada',
            appointments_status_cancelled: 'Cancelada',
            appointments_mark_done: 'Marcar como realizada',
            appointments_cancel: 'Cancelar consulta',
            
            // Configurações de Alertas
            alerts_config_title: 'Alertas de Medicação',
            alerts_first_delay: 'Primeiro alerta após',
            alerts_second_delay: 'Segundo alerta após',
            alerts_escalation: 'Avisar cuidadores após',
            alerts_minutes: 'minutos',
            alerts_notify_sound: 'Som de alerta',
            alerts_notify_vibration: 'Vibração',
            alerts_notify_caregivers: 'Notificar cuidadores',
            alerts_notify_sms: 'Enviar SMS',
            alerts_notify_whatsapp: 'Enviar WhatsApp',
            alerts_notify_push: 'Notificação push',
            alerts_select_caregivers: 'Cuidadores a notificar',
            alerts_enabled: 'Alertas ativos',
            alerts_disabled: 'Alertas desativados',
            
            // Dias da semana
            day_sunday: 'Domingo',
            day_monday: 'Segunda',
            day_tuesday: 'Terça',
            day_wednesday: 'Quarta',
            day_thursday: 'Quinta',
            day_friday: 'Sexta',
            day_saturday: 'Sábado',
            
            // Meses
            month_jan: 'Janeiro',
            month_feb: 'Fevereiro',
            month_mar: 'Março',
            month_apr: 'Abril',
            month_may: 'Maio',
            month_jun: 'Junho',
            month_jul: 'Julho',
            month_aug: 'Agosto',
            month_sep: 'Setembro',
            month_oct: 'Outubro',
            month_nov: 'Novembro',
            month_dec: 'Dezembro',
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
            add: 'Add',
            edit: 'Edit',
            delete: 'Delete',
            undo: 'Undo',
            
            // Greetings
            greeting_morning: 'Good morning',
            greeting_afternoon: 'Good afternoon',
            greeting_evening: 'Good evening',
            
            // Home screen
            home_companion: 'Chat',
            home_medication: 'Medication',
            home_family: 'Family',
            home_routine: 'Routine',
            home_appointments: 'Appointments',
            home_health: 'Health',
            home_status_ok: 'Everything is fine!',
            home_status_check: 'Last check a moment ago',
            next_reminder: 'Next reminder',
            
            // Medication
            medication_title: "Today's Medication",
            medication_pending: 'Pending',
            medication_taken: 'Already taken',
            medication_take_btn: 'Taken',
            medication_undo_btn: "Didn't take",
            medication_all_taken: 'Congratulations!',
            medication_all_taken_msg: "You've taken all medication for today",
            medication_at: 'at',
            medication_missed: 'Medication overdue',
            medication_missed_msg: "It's time to take your medication",
            
            // Appointments
            appointments_title: 'Appointments',
            appointments_upcoming: 'Upcoming',
            appointments_past: 'Past appointments',
            appointments_add: 'Add appointment',
            appointments_none: 'No appointments scheduled',
            appointments_doctor: 'Doctor/Specialty',
            appointments_date: 'Date',
            appointments_time: 'Time',
            appointments_location: 'Location',
            appointments_notes: 'Notes',
            appointments_done: 'Completed',
            appointments_mark_done: 'Mark as completed',
            
            // Health Records
            health_title: 'Health Records',
            health_add: 'New record',
            health_blood_pressure: 'Blood Pressure',
            health_blood_pressure_sys: 'Systolic (max)',
            health_blood_pressure_dia: 'Diastolic (min)',
            health_heart_rate: 'Heart Rate',
            health_glucose: 'Blood Glucose',
            health_weight: 'Weight',
            health_temperature: 'Temperature',
            health_oxygen: 'Blood Oxygen',
            health_unit_mmhg: 'mmHg',
            health_unit_bpm: 'bpm',
            health_unit_mgdl: 'mg/dL',
            health_unit_kg: 'kg',
            health_unit_celsius: '°C',
            health_unit_percent: '%',
            health_history: 'History',
            health_no_records: 'No records',
            health_last_record: 'Last record',
            
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
            settings_notifications: 'Notifications',
            settings_notifications_desc: 'Configure family alerts',
            settings_notify_all: 'All notifications',
            settings_notify_medication: 'Only medication misses',
            settings_notify_emergency: 'Only emergencies',
            settings_notify_none: 'None',
            settings_notify_family_label: 'Alert family when:',
            settings_profile: 'Profile',
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
            error_fill_fields: 'Please fill in required fields',
            
            // Success
            success_saved: 'Saved successfully',
            success_recorded: 'Recorded successfully',
            
            // Appointments
            appointments_title: 'Appointments',
            appointments_upcoming: 'Upcoming Appointments',
            appointments_past: 'Past Appointments',
            appointments_add: 'Schedule Appointment',
            appointments_no_upcoming: 'No appointments scheduled',
            appointments_doctor: 'Doctor',
            appointments_specialty: 'Specialty',
            appointments_location: 'Location',
            appointments_date: 'Date',
            appointments_time: 'Time',
            appointments_notes: 'Notes',
            appointments_reminder: 'Reminder',
            appointments_hours_before: 'hours before',
            appointments_status_scheduled: 'Scheduled',
            appointments_status_completed: 'Completed',
            appointments_status_cancelled: 'Cancelled',
            appointments_mark_done: 'Mark as completed',
            appointments_cancel: 'Cancel appointment',
            
            // Alert Configuration
            alerts_config_title: 'Medication Alerts',
            alerts_first_delay: 'First alert after',
            alerts_second_delay: 'Second alert after',
            alerts_escalation: 'Notify caregivers after',
            alerts_minutes: 'minutes',
            alerts_notify_sound: 'Alert sound',
            alerts_notify_vibration: 'Vibration',
            alerts_notify_caregivers: 'Notify caregivers',
            alerts_notify_sms: 'Send SMS',
            alerts_notify_whatsapp: 'Send WhatsApp',
            alerts_notify_push: 'Push notification',
            alerts_select_caregivers: 'Caregivers to notify',
            alerts_enabled: 'Alerts enabled',
            alerts_disabled: 'Alerts disabled',
            
            // Days
            day_sunday: 'Sunday',
            day_monday: 'Monday',
            day_tuesday: 'Tuesday',
            day_wednesday: 'Wednesday',
            day_thursday: 'Thursday',
            day_friday: 'Friday',
            day_saturday: 'Saturday',
            
            // Months
            month_jan: 'January',
            month_feb: 'February',
            month_mar: 'March',
            month_apr: 'April',
            month_may: 'May',
            month_jun: 'June',
            month_jul: 'July',
            month_aug: 'August',
            month_sep: 'September',
            month_oct: 'October',
            month_nov: 'November',
            month_dec: 'December',
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
            add: 'Añadir',
            edit: 'Editar',
            delete: 'Eliminar',
            undo: 'Deshacer',
            
            // Greetings
            greeting_morning: 'Buenos días',
            greeting_afternoon: 'Buenas tardes',
            greeting_evening: 'Buenas noches',
            
            // Home screen
            home_companion: 'Conversar',
            home_medication: 'Medicación',
            home_family: 'Familia',
            home_routine: 'Rutina',
            home_appointments: 'Citas',
            home_health: 'Salud',
            home_status_ok: '¡Todo está bien!',
            home_status_check: 'Última comprobación hace un momento',
            next_reminder: 'Próximo recordatorio',
            
            // Medication
            medication_title: 'Medicación de Hoy',
            medication_pending: 'Pendiente',
            medication_taken: 'Ya tomados',
            medication_take_btn: 'Tomado',
            medication_undo_btn: 'No tomé',
            medication_all_taken: '¡Felicidades!',
            medication_all_taken_msg: 'Ha tomado toda la medicación de hoy',
            medication_at: 'a las',
            medication_missed: 'Medicación retrasada',
            medication_missed_msg: 'Es hora de tomar su medicación',
            
            // Appointments
            appointments_title: 'Citas',
            appointments_upcoming: 'Próximas citas',
            appointments_past: 'Citas anteriores',
            appointments_add: 'Añadir cita',
            appointments_none: 'Sin citas programadas',
            appointments_doctor: 'Médico/Especialidad',
            appointments_date: 'Fecha',
            appointments_time: 'Hora',
            appointments_location: 'Lugar',
            appointments_notes: 'Notas',
            appointments_done: 'Completada',
            appointments_mark_done: 'Marcar como completada',
            
            // Health Records
            health_title: 'Registros de Salud',
            health_add: 'Nuevo registro',
            health_blood_pressure: 'Tensión Arterial',
            health_blood_pressure_sys: 'Sistólica (máx)',
            health_blood_pressure_dia: 'Diastólica (mín)',
            health_heart_rate: 'Frecuencia Cardíaca',
            health_glucose: 'Glucemia',
            health_weight: 'Peso',
            health_temperature: 'Temperatura',
            health_oxygen: 'Oxígeno en Sangre',
            health_unit_mmhg: 'mmHg',
            health_unit_bpm: 'ppm',
            health_unit_mgdl: 'mg/dL',
            health_unit_kg: 'kg',
            health_unit_celsius: '°C',
            health_unit_percent: '%',
            health_history: 'Historial',
            health_no_records: 'Sin registros',
            health_last_record: 'Último registro',
            
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
            settings_notifications: 'Notificaciones',
            settings_notifications_desc: 'Configurar alertas familiares',
            settings_notify_all: 'Todas las notificaciones',
            settings_notify_medication: 'Solo faltas de medicación',
            settings_notify_emergency: 'Solo emergencias',
            settings_notify_none: 'Ninguna',
            settings_notify_family_label: 'Alertar familia cuando:',
            settings_profile: 'Perfil',
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
            
            // Days
            day_sunday: 'Domingo',
            day_monday: 'Lunes',
            day_tuesday: 'Martes',
            day_wednesday: 'Miércoles',
            day_thursday: 'Jueves',
            day_friday: 'Viernes',
            day_saturday: 'Sábado',
            
            // Months
            month_jan: 'Enero',
            month_feb: 'Febrero',
            month_mar: 'Marzo',
            month_apr: 'Abril',
            month_may: 'Mayo',
            month_jun: 'Junio',
            month_jul: 'Julio',
            month_aug: 'Agosto',
            month_sep: 'Septiembre',
            month_oct: 'Octubre',
            month_nov: 'Noviembre',
            month_dec: 'Diciembre',
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
            add: 'Ajouter',
            edit: 'Modifier',
            delete: 'Supprimer',
            undo: 'Annuler',
            
            // Greetings
            greeting_morning: 'Bonjour',
            greeting_afternoon: 'Bon après-midi',
            greeting_evening: 'Bonsoir',
            
            // Home screen
            home_companion: 'Discuter',
            home_medication: 'Médicaments',
            home_family: 'Famille',
            home_routine: 'Routine',
            home_appointments: 'Rendez-vous',
            home_health: 'Santé',
            home_status_ok: 'Tout va bien !',
            home_status_check: 'Dernière vérification il y a un instant',
            next_reminder: 'Prochain rappel',
            
            // Medication
            medication_title: "Médicaments d'Aujourd'hui",
            medication_pending: 'À prendre',
            medication_taken: 'Déjà pris',
            medication_take_btn: 'Pris',
            medication_undo_btn: "Pas pris",
            medication_all_taken: 'Félicitations !',
            medication_all_taken_msg: "Vous avez pris tous vos médicaments aujourd'hui",
            medication_at: 'à',
            medication_missed: 'Médicament en retard',
            medication_missed_msg: "C'est l'heure de prendre votre médicament",
            
            // Appointments
            appointments_title: 'Rendez-vous',
            appointments_upcoming: 'Prochains rendez-vous',
            appointments_past: 'Rendez-vous passés',
            appointments_add: 'Ajouter rendez-vous',
            appointments_none: 'Aucun rendez-vous prévu',
            appointments_doctor: 'Médecin/Spécialité',
            appointments_date: 'Date',
            appointments_time: 'Heure',
            appointments_location: 'Lieu',
            appointments_notes: 'Notes',
            appointments_done: 'Effectué',
            appointments_mark_done: 'Marquer comme effectué',
            
            // Health Records
            health_title: 'Dossiers de Santé',
            health_add: 'Nouveau dossier',
            health_blood_pressure: 'Tension Artérielle',
            health_blood_pressure_sys: 'Systolique (max)',
            health_blood_pressure_dia: 'Diastolique (min)',
            health_heart_rate: 'Fréquence Cardiaque',
            health_glucose: 'Glycémie',
            health_weight: 'Poids',
            health_temperature: 'Température',
            health_oxygen: 'Oxygène Sanguin',
            health_unit_mmhg: 'mmHg',
            health_unit_bpm: 'bpm',
            health_unit_mgdl: 'mg/dL',
            health_unit_kg: 'kg',
            health_unit_celsius: '°C',
            health_unit_percent: '%',
            health_history: 'Historique',
            health_no_records: 'Aucun dossier',
            health_last_record: 'Dernier dossier',
            
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
            settings_notifications: 'Notifications',
            settings_notifications_desc: 'Configurer les alertes familiales',
            settings_notify_all: 'Toutes les notifications',
            settings_notify_medication: 'Médicaments manqués uniquement',
            settings_notify_emergency: 'Urgences uniquement',
            settings_notify_none: 'Aucune',
            settings_notify_family_label: 'Alerter la famille quand:',
            settings_profile: 'Profil',
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
            
            // Days
            day_sunday: 'Dimanche',
            day_monday: 'Lundi',
            day_tuesday: 'Mardi',
            day_wednesday: 'Mercredi',
            day_thursday: 'Jeudi',
            day_friday: 'Vendredi',
            day_saturday: 'Samedi',
            
            // Months
            month_jan: 'Janvier',
            month_feb: 'Février',
            month_mar: 'Mars',
            month_apr: 'Avril',
            month_may: 'Mai',
            month_jun: 'Juin',
            month_jul: 'Juillet',
            month_aug: 'Août',
            month_sep: 'Septembre',
            month_oct: 'Octobre',
            month_nov: 'Novembre',
            month_dec: 'Décembre',
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
            add: 'Hinzufügen',
            edit: 'Bearbeiten',
            delete: 'Löschen',
            undo: 'Rückgängig',
            
            // Greetings
            greeting_morning: 'Guten Morgen',
            greeting_afternoon: 'Guten Tag',
            greeting_evening: 'Guten Abend',
            
            // Home screen
            home_companion: 'Plaudern',
            home_medication: 'Medikamente',
            home_family: 'Familie',
            home_routine: 'Tagesablauf',
            home_appointments: 'Termine',
            home_health: 'Gesundheit',
            home_status_ok: 'Alles ist in Ordnung!',
            home_status_check: 'Letzte Überprüfung vor kurzem',
            next_reminder: 'Nächste Erinnerung',
            
            // Medication
            medication_title: 'Heutige Medikamente',
            medication_pending: 'Ausstehend',
            medication_taken: 'Bereits genommen',
            medication_take_btn: 'Genommen',
            medication_undo_btn: 'Nicht genommen',
            medication_all_taken: 'Herzlichen Glückwunsch!',
            medication_all_taken_msg: 'Sie haben heute alle Medikamente genommen',
            medication_at: 'um',
            medication_missed: 'Medikament überfällig',
            medication_missed_msg: 'Es ist Zeit für Ihr Medikament',
            
            // Appointments
            appointments_title: 'Termine',
            appointments_upcoming: 'Bevorstehende Termine',
            appointments_past: 'Vergangene Termine',
            appointments_add: 'Termin hinzufügen',
            appointments_none: 'Keine Termine geplant',
            appointments_doctor: 'Arzt/Fachgebiet',
            appointments_date: 'Datum',
            appointments_time: 'Uhrzeit',
            appointments_location: 'Ort',
            appointments_notes: 'Notizen',
            appointments_done: 'Erledigt',
            appointments_mark_done: 'Als erledigt markieren',
            
            // Health Records
            health_title: 'Gesundheitsdaten',
            health_add: 'Neuer Eintrag',
            health_blood_pressure: 'Blutdruck',
            health_blood_pressure_sys: 'Systolisch (max)',
            health_blood_pressure_dia: 'Diastolisch (min)',
            health_heart_rate: 'Herzfrequenz',
            health_glucose: 'Blutzucker',
            health_weight: 'Gewicht',
            health_temperature: 'Temperatur',
            health_oxygen: 'Blutsauerstoff',
            health_unit_mmhg: 'mmHg',
            health_unit_bpm: 'bpm',
            health_unit_mgdl: 'mg/dL',
            health_unit_kg: 'kg',
            health_unit_celsius: '°C',
            health_unit_percent: '%',
            health_history: 'Verlauf',
            health_no_records: 'Keine Einträge',
            health_last_record: 'Letzter Eintrag',
            
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
            settings_notifications: 'Benachrichtigungen',
            settings_notifications_desc: 'Familienalarme konfigurieren',
            settings_notify_all: 'Alle Benachrichtigungen',
            settings_notify_medication: 'Nur versäumte Medikamente',
            settings_notify_emergency: 'Nur Notfälle',
            settings_notify_none: 'Keine',
            settings_notify_family_label: 'Familie benachrichtigen bei:',
            settings_profile: 'Profil',
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
            
            // Days
            day_sunday: 'Sonntag',
            day_monday: 'Montag',
            day_tuesday: 'Dienstag',
            day_wednesday: 'Mittwoch',
            day_thursday: 'Donnerstag',
            day_friday: 'Freitag',
            day_saturday: 'Samstag',
            
            // Months
            month_jan: 'Januar',
            month_feb: 'Februar',
            month_mar: 'März',
            month_apr: 'April',
            month_may: 'Mai',
            month_jun: 'Juni',
            month_jul: 'Juli',
            month_aug: 'August',
            month_sep: 'September',
            month_oct: 'Oktober',
            month_nov: 'November',
            month_dec: 'Dezember',
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
            add: 'Aggiungi',
            edit: 'Modifica',
            delete: 'Elimina',
            undo: 'Annulla',
            
            // Greetings
            greeting_morning: 'Buongiorno',
            greeting_afternoon: 'Buon pomeriggio',
            greeting_evening: 'Buonasera',
            
            // Home screen
            home_companion: 'Chiacchierare',
            home_medication: 'Medicinali',
            home_family: 'Famiglia',
            home_routine: 'Routine',
            home_appointments: 'Appuntamenti',
            home_health: 'Salute',
            home_status_ok: 'Tutto bene!',
            home_status_check: 'Ultimo controllo poco fa',
            next_reminder: 'Prossimo promemoria',
            
            // Medication
            medication_title: 'Medicinali di Oggi',
            medication_pending: 'Da prendere',
            medication_taken: 'Già presi',
            medication_take_btn: 'Preso',
            medication_undo_btn: 'Non preso',
            medication_all_taken: 'Complimenti!',
            medication_all_taken_msg: 'Hai preso tutti i medicinali di oggi',
            medication_at: 'alle',
            medication_missed: 'Medicinale in ritardo',
            medication_missed_msg: 'È ora di prendere il medicinale',
            
            // Appointments
            appointments_title: 'Appuntamenti',
            appointments_upcoming: 'Prossimi appuntamenti',
            appointments_past: 'Appuntamenti passati',
            appointments_add: 'Aggiungi appuntamento',
            appointments_none: 'Nessun appuntamento programmato',
            appointments_doctor: 'Medico/Specialità',
            appointments_date: 'Data',
            appointments_time: 'Ora',
            appointments_location: 'Luogo',
            appointments_notes: 'Note',
            appointments_done: 'Completato',
            appointments_mark_done: 'Segna come completato',
            
            // Health Records
            health_title: 'Dati Sanitari',
            health_add: 'Nuovo registro',
            health_blood_pressure: 'Pressione Sanguigna',
            health_blood_pressure_sys: 'Sistolica (max)',
            health_blood_pressure_dia: 'Diastolica (min)',
            health_heart_rate: 'Frequenza Cardiaca',
            health_glucose: 'Glicemia',
            health_weight: 'Peso',
            health_temperature: 'Temperatura',
            health_oxygen: 'Ossigeno nel Sangue',
            health_unit_mmhg: 'mmHg',
            health_unit_bpm: 'bpm',
            health_unit_mgdl: 'mg/dL',
            health_unit_kg: 'kg',
            health_unit_celsius: '°C',
            health_unit_percent: '%',
            health_history: 'Cronologia',
            health_no_records: 'Nessun registro',
            health_last_record: 'Ultimo registro',
            
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
            settings_notifications: 'Notifiche',
            settings_notifications_desc: 'Configura avvisi familiari',
            settings_notify_all: 'Tutte le notifiche',
            settings_notify_medication: 'Solo medicinali mancati',
            settings_notify_emergency: 'Solo emergenze',
            settings_notify_none: 'Nessuna',
            settings_notify_family_label: 'Avvisa famiglia quando:',
            settings_profile: 'Profilo',
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
            
            // Days
            day_sunday: 'Domenica',
            day_monday: 'Lunedì',
            day_tuesday: 'Martedì',
            day_wednesday: 'Mercoledì',
            day_thursday: 'Giovedì',
            day_friday: 'Venerdì',
            day_saturday: 'Sabato',
            
            // Months
            month_jan: 'Gennaio',
            month_feb: 'Febbraio',
            month_mar: 'Marzo',
            month_apr: 'Aprile',
            month_may: 'Maggio',
            month_jun: 'Giugno',
            month_jul: 'Luglio',
            month_aug: 'Agosto',
            month_sep: 'Settembre',
            month_oct: 'Ottobre',
            month_nov: 'Novembre',
            month_dec: 'Dicembre',
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
