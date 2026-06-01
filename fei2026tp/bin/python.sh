#!/bin/bash
set -e

cd "$(dirname "$0")/.."
sudo docker compose exec django python "$@"
