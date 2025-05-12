# Scratchpad: Future Considerations & Potential Pitfalls

## Web Portal Development
- **Docker Workflow:** Consider using Docker Compose for easy deployment and updates.
- **Reverse Proxy:** Use Synology's Application Portal to map domains to your containers.
- **Persistent Storage:** Mount NAS folders into containers for logs, uploads, and data.
- **Security:** Use HTTPS, user management, and possibly VPN for secure access.
- **Development Options:**
  - Local development + Git + Docker Compose deployment.
  - Remote development via SSH or Synology's Text Editor/Code Server.
  - CI/CD pipeline for automated deployments.

## Potential Pitfalls
- **Permissions:** Ensure Docker containers have the right PUID/PGID and folder permissions.
- **Updates:** Manual DSM/package updates to avoid breaking Docker setups.
- **Storage:** Monitor disk space, especially with media and Docker images.
- **Network:** Ensure synobridge network is correctly configured for inter-container communication.
- **Backup:** Regularly backup Docker configs, shared folders, and critical data.
- **Performance:** Monitor CPU, RAM, and disk I/O, especially with hardware transcoding and multiple containers.

## Future Enhancements
- **Dashboard:** Develop a web portal for monitoring and managing NAS services.
- **Automation:** Use scripts or CI/CD for automated deployments and updates.
- **Scaling:** Plan for future storage expansion or additional services.

## Working Permission Structure (May 11, 2024)
### Prowlarr Folder Structure (Reference for Correct Permissions)
```
drwxrwxrwx+ 1 dockeruser docker    254 May 11 18:25 .
drwxrwxrwx+ 1 root       root      100 May 11 17:47 ..
drwxrwxrwx+ 1 dockeruser docker     88 May 11 13:31 asp
-rwxrwxrwx+ 1 dockeruser docker    575 May 11 13:32 config.xml
drwxrwxrwx+ 1 dockeruser docker  14454 May 11 13:31 Definitions
drwxrwxrwx+ 1 dockeruser docker     60 May 11 13:31 logs
-rwxrwxrwx+ 1 dockeruser docker  90112 May 11 18:24 logs.db
-rwxrwxrwx+ 1 dockeruser docker 241664 May 11 18:25 prowlarr.db
-rwxrwxrwx+ 1 dockeruser docker  32768 May 11 18:33 prowlarr.db-shm
-rwxrwxrwx+ 1 dockeruser docker 148352 May 11 18:33 prowlarr.db-wal
-rwxrwxrwx+ 1 dockeruser docker    608 May 11 18:36 prowlarr-flaresolverr-compose.yml
-rwxrwxrwx+ 1 dockeruser docker      3 May 11 13:31 prowlarr.
```

Key points:
- All files and directories owned by `dockeruser:docker`
- All directories have `drwxrwxrwx+` (777 with ACL)
- All files have `-rwxrwxrwx+` (777 with ACL)
- This structure allows both Docker container and admin user access 