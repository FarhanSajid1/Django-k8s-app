resource "google_container_cluster" "default" {
    name                = "${var.name}"
    network             = "${var.network}"
    subnetwork          = "${var.subnetwork}"
    zone                = "${var.zone}"

    additional_zones     = "${var.additional_zones}"

    master_auth {
        username        = "${var.username}"
        password        = "${length(var.password) > 0 ? var.password : random_string.password.result}"
    }

    initial_node_count  = "${var.initial_node_count}"

    node_config {
        machine_type    = "${var.machine_type}" 
        oauth_scopes    = [
            "https://www.googleapis.com/auth/compute",
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring",
        ]
    }
}

resource "random_string" "password" {
    length  = 16
    special = true
    number  = true
    lower   = true
    upper   = true
}

