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