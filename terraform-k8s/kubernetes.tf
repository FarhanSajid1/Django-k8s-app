provider "google" {
  credentials = "${file("credentials.json")}"
  project = "default-239304"
  region = "us-east-1"
}


resource "google_container_cluster" "django-cluster" {
  name = "django-k8s"
  network = "default"
  zone = "us-east1-b"
  initial_node_count = 3
}

