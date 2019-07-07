from flask import Flask, make_response, url_for, request
import os
import subprocess

app = Flask(__name__)

host_ipaddr=os.environ["RPI_PROVISION_IPADDR"]
host_port=int(os.environ["RPI_PROVISION_PORT"])

@app.route("/")
def entry():
    return make_response("Request provisioning for a host by sending a POST to {}")#.format(url_for("v0/checkin")))

# TODO: require authentication of the POST request
@app.route("/v0/checkin/", methods=["GET", "POST"])
def checkin():
    if request.method == 'POST':
        data = request.get_json()
        # TODO: remote ipaddr should be passed from the pi rather than implicitly assumed from the http request,
        # in case there is a router in between.
        output = subprocess.check_output(["ansible-playbook", "-i", "{},".format(request.remote_addr), "-u", data["ssh_user"], "playbook-rpi-provision.yml"])
        # TODO: format the output more nicely. For now just prints the raw bytes of the ansible-playbook output.
        print(output)
        return make_response("Host at {} has checked in, starting provisioning for user {} on port {}...\n".format(request.remote_addr, data["ssh_user"], data["ssh_port"]))
    else:
        return make_response("Send a POST request to check in a host for provisioning.\n")

if __name__ == "__main__":
    app.run(host=host_ipaddr, port=host_port)
