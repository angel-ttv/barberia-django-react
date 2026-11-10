# Nivara Barber Shop System — Frontend (React + Vite PWA)

Interfaz para el dueño/barbero: agenda del día, agendar citas, cerrar y cobrar, y corte de caja. Funciona offline (guarda citas en IndexedDB si no hay internet y las sincroniza solo cuando vuelve la conexión).

## 1. Instalación

Requiere Node.js 18+ y el backend corriendo (ver `nivara_barber_backend/README.md`).

```bash
npm install
cp .env.example .env      # ajusta VITE_API_BASE si el backend no está en localhost:8000
npm run dev
```

Abre `http://localhost:5173`. Inicia sesión con el usuario que creaste con `createsuperuser` en el backend (o cualquier usuario de Django con acceso).

## 2. Qué incluye

- **Login** por token (usa el endpoint `/api/auth-token/` del backend).
- **Agenda**: lista de citas del día, filtrable por fecha. Confirmar, cancelar, y "Cerrar y cobrar" en un solo paso.
- **Nueva cita**: formulario con barbero, servicio, cliente y horario.
- **Corte de caja**: ventas, comisión y pendiente de retiro por barbero/día, con botón para marcar la comisión como retirada.
- **Modo offline**: si creas una cita sin internet, se guarda en IndexedDB de tu navegador y se sincroniza sola en cuanto vuelve la conexión (lo verás como "X por sincronizar" en la barra superior). El *app shell* (HTML/JS/CSS) también se cachea con un Service Worker, así que la app abre aunque no haya internet en ese momento.

## 3. Build de producción

```bash
npm run build
```

Genera la carpeta `dist/` lista para subir a cualquier hosting estático (o servirla desde el mismo VPS con Coolify/Nginx). Configura `VITE_API_BASE` apuntando al dominio real de tu backend antes de compilar.

## 4. Qué falta para el MVP completo (Fase 1-2 del roadmap)

- Enlace público de reservas para que el cliente agende sin login (hoy todo el flujo requiere iniciar sesión como dueño/barbero).
- Notificaciones/recordatorios de WhatsApp (se conectan del lado del backend).
- Pantalla de gestión de barberos y servicios desde la UI (hoy se administran desde `/admin/` de Django).
- Vista de reportes/ingresos más allá del corte de caja diario.
