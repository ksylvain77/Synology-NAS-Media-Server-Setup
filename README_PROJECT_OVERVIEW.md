# Project Overview & Setup Guide

## 1. Project Purpose
This project is designed to manage and automate media downloads, organization, and streaming using a Synology NAS and a suite of Dockerized applications. It provides a robust, reproducible setup for running Radarr, Sonarr, Prowlarr, qBittorrent, and Plex, with all configuration and data stored on the NAS for easy backup and management.

---

## 2. NAS & Storage Structure
- **Device:** Synology NAS (BTRFS filesystem)
- **Main storage paths:**
  - `/volume1/configs` — All Docker app configs
  - `/volume1/data` — Media libraries (e.g., movies, tv)
  - `/volume1/downloads` — Downloaded files (torrents, usenet, etc.)

### Example Folder Layout
```
/volume1/configs/
  ├── radarr/
  ├── sonarr/
  ├── prowlarr/
  ├── qbittorrent/
  ├── plex/
  └── recyclarr2/
/volume1/data/
  ├── movies/
  └── tv/
/volume1/downloads/
  └── torrents/
```

---

## 3. Permissions & Users
- **Docker containers run as:**
  - User: `dockeruser` (UID: 1027)
  - Group: `docker` (GID: 65536)
- **Permissions:**
  - All config and data folders should be owned by `dockeruser:docker` and set to `777` for maximum compatibility.
  - Example command:
    ```bash
    sudo chown -R dockeruser:docker /volume1/configs/[app]
    sudo chmod -R 777 /volume1/configs/[app]
    ```
- **Admin user:** `kevin` (for DSM/web UI access)

---

## 4. Docker Compose & Container Setup
- Each app has its own `docker-compose.yml` (or similar) in the `configs/[app]/` directory.
- **Common environment variables:**
  - `PUID=1027`
  - `PGID=65536`
  - `TZ=America/New_York` (or your timezone)
- **Volume mappings:**
  - `/volume1/configs/[app]:/config` (app config)
  - `/volume1/data/[type]:/[type]` (media libraries)
  - `/volume1/downloads:/downloads` (downloads)
- **Network:**
  - All containers use the `synobridge` Docker network for inter-container communication.

---

## 5. Application Credentials & URLs
- **Sonarr:**
  - URL: `http://192.168.50.92:8989`
  - API Key: (see `star_apps_info.md`)
- **Radarr:**
  - URL: `http://192.168.50.92:7878`
  - API Key: (see `star_apps_info.md`)
- **Prowlarr:**
  - URL: `http://192.168.50.92:9696`
  - API Key: (see `star_apps_info.md`)
- **qBittorrent:**
  - URL: `http://192.168.50.92:8080/`
  - Username: `kevin`
  - Password: `kevinkevin`
- **Plex:**
  - (See your Plex account for details)

---

## 6. Best Practices & Notes
- **Backups:** Regularly back up `/volume1/configs` and `/volume1/data`.
- **Updates:** Use Docker Compose to update containers. Always check release notes for breaking changes.
- **Security:**
  - Use strong passwords for all web UIs.
  - Restrict access to the NAS and Docker apps to trusted networks.
- **Troubleshooting:**
  - Check container logs with `sudo docker logs [container]`.
  - Use `ls -l` and `id` to verify permissions and user mappings.
- **Documentation:**
  - All API keys, credentials, and URLs are documented in `configs/star_apps_info.md`.
  - User and group IDs are documented in `configs/docker_user_info.md`.
  - Storage and permission structure is documented in `configs/nas_storage_config.md`.

---

## 7. Getting Started
1. Set up your folder structure on the NAS as shown above.
2. Set permissions and ownership for all config and data folders.
3. Copy and customize the Docker Compose files for each app.
4. Start each container with Docker Compose or the Synology Docker UI.
5. Access each app via its web UI and complete any in-app setup.
6. Refer to the `star_apps_info.md` for API keys and credentials.

---

## 8. References
- [TRaSH Guides](https://trash-guides.info/)
- [DrFrankenstein's Docker Guides](https://drfrankenstein.co.uk/)
- [Official App Docs: Radarr, Sonarr, Prowlarr, qBittorrent, Plex]

---

This document serves as a comprehensive starting point for setting up and maintaining a Synology NAS-based media automation stack using Docker. Update as your environment evolves. 