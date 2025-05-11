# Docker User & Group Info

- **Username:** dockeruser
- **PUID (UID):** 1027
- **PGID (GID for docker group):** 65536

Use these values in your Docker Compose files for correct permissions:

```yaml
PUID: 1027
PGID: 65536
``` 