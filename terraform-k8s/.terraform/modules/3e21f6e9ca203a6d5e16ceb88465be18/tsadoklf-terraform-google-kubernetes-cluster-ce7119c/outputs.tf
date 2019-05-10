output "endpoint" {
    value = "${google_container_cluster.default.endpoint}"
}
output "group_urls" {
    value = "${google_container_cluster.default.instance_group_urls}"
}
output "node_config" {
    value = "${google_container_cluster.default.node_config}"
}
output "node_pool" {
    value = "${google_container_cluster.default.node_pool}"
}
output "username" {
    value = "${google_container_cluster.default.master_auth.0.username}"
}
output "password" {
    value = "${google_container_cluster.default.master_auth.0.password}"
}
output "client_certificate" {
    value = "${google_container_cluster.default.master_auth.0.client_certificate}"
}
output "client_key" {
    value = "${google_container_cluster.default.master_auth.0.client_key}"
}
output "cluster_ca_certificate" {
    value = "${google_container_cluster.default.master_auth.0.cluster_ca_certificate}"
}
