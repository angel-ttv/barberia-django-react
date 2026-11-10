# Nivara Barber Shop System — Django + React PWA (rescatado 6 nov 2026)

Sistema completo para barbería, más serio que la versión Firebase en HTML.

## Backend (Django + DRF) — solo fragmentos rescatados
- `manage.py` — settings `nivara_barber.settings`
- `urls.py` — API: barbers, services, appointments, payments + webhook `whatsapp/webhook/`
- FALTA: el resto del backend (`settings.py`, `views.py`, `models.py`, etc. — ver `nivara_barber_backend/README.md`, no se subió).

## Frontend (React 19 + Vite PWA) — solo fragmentos rescatados
- `README-3.md` — instrucciones: agenda del día, agendar, cerrar y cobrar, corte de caja con comisiones por barbero, login por token (`/api/auth-token/`), modo offline con IndexedDB + Service Worker.
- `package-lock.json` — `nivara_barber_frontend`, React 19.2.8.
- FALTA: el código fuente (`src/`, `package.json`, `.env.example`).

## Pendiente del MVP (según su README)
- Enlace público de reservas sin login.
- Recordatorios por WhatsApp.
- Gestión de barberos y servicios desde la UI.
- Reportes de ingresos más allá del corte diario.
