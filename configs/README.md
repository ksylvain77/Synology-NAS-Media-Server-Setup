# Docker Compose Configurations

This directory contains all the Docker Compose YAML configurations for the Synology NAS setup.

## Directory Structure
- `yaml/` - Contains all the YAML configuration files
  - `arrs-compose.yml` - Arrs Media Project configuration
  - `plex-compose.yml` - Plex with hardware transcoding
  - `qbittorrent-compose.yml` - qBittorrent configuration
  - `watchtower-compose.yml` - Container update automation

## Usage
These configurations are templates that will be customized during the setup process with:
- PUID and PGID from the restricted Docker user
- Timezone settings
- Network configurations
- Volume mappings

## Notes
- All configurations use the `synobridge` network for inter-container communication
- Configurations are designed to work with the directory structure created in the initial setup
- Some configurations may require additional customization based on specific needs 