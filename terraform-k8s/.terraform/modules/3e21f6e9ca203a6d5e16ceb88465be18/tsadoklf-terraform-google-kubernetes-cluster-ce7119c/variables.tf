
variable "name" {
    type        = "string"
    description = "The cluster name."
}
variable "network" {
    type        = "string"
    description = ""
}
variable "subnetwork" {
    type        = "string"
    description = ""
}
variable "zone" {
    type        = "string"
    description = ""
}
variable "additional_zones" {
    type        = "list"
    description = ""
    default     = []
    
}
variable "username" {
    type        = "string"
    description = ""
    default     = "admin"
}
variable "password" {
    type        = "string"
    description = ""
    default     = ""
}
variable "initial_node_count" {
    type        = "string"
    description = ""
    default     = "1"
}
variable "machine_type" {
    type        = "string"
    description = "The machine type of the cluster's nodes"
    default     = "n1-standard-1"
}
