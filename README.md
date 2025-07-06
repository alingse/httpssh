# httpssh
ssh client via http request

## TODO List (from Gemini CLI conversation)

### User Story
As a developer, when my private service is down, I need a secure, web-based SSH terminal with HTTPS support to quickly log in and perform emergency fixes from any computer, without needing a local SSH client.

### Key Requirements & Considerations

*   **Primary Use Case:** Emergency access and quick fixes on private services from company computers.
*   **Target Users:** Primarily the user themselves, and other trusted, interested developers.
*   **Access Level:** Root or sudo privileges are required.
*   **Command Restrictions:** No command restrictions should be imposed.
*   **Authentication & Link Management:**
    *   For personal use: Preference for a fixed URL with basic password authentication.
    *   For sharing with other developers: Clarify if a similar fixed URL + basic password is desired, or if a temporary/one-time link mechanism is still preferred.
*   **Security (High Priority):**
    *   **HTTPS:** Mandatory for all communication.
    *   **Session Management:**
        *   Automatic session timeout.
        *   Session termination upon browser close.
    *   **Auditing/Logging:** Clarify if logging of executed commands is desired for high-privilege sessions.
    *   **IP Restriction:** Clarify if restricting access to specific IP addresses is desired.
*   **Core Functionality:**
    *   **WebSocket:** Essential for interactive shell experience.
    *   **PTY (Pseudo-Terminal):** For proper terminal emulation.
    *   **Frontend Terminal Emulator:** (e.g., `xterm.js`) for rendering and input.
*   **Additional Features (To be clarified):**
    *   File upload/download.
    *   Multi-session support.
    *   Terminal customization (themes, fonts).
    *   Clipboard integration.

### Design Decisions (from Gemini CLI conversation)

*   **User Interface:**
    *   **Login Page:** Minimalist design (username/password input only).
    *   **Terminal Page:** Pure terminal interface, no additional UI elements.
*   **Management Interface:**
    *   **Purpose:** Manage link paths, passwords, active SSH sessions, and view logs.
    *   **Access:** Accessible via a dedicated Web URL (e.g., `/admin`) and directly editable via configuration files.
    *   **Security:** Independent administrator authentication (username/password) is required, with consideration for Two-Factor Authentication (2FA).
