# rpi-provision

Provisioning server for Raspberry Pi images.

Typically for use with images produced by [rpi-bootstrap](https://github.com/rfairley/rpi-bootstrap).

Example run:

```
python3 -m venv rpi_provision
source rpi_provision/bin/activate
RPI_PROVISION_IPADDR=127.0.0.1 RPI_PROVISION_PORT=5000 python3 provision.py
```
