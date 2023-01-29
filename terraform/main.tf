


resource "gcp_container_cluster" "monitoramento-app" {
  name               = "monitoramento-app"
  zone               = "us-central1-a"
  initial_node_count = 1
  enable_autoupgrade = true
  enable_basic_auth  = false
  issue_client_certificate = false
  enable_ip_alias = true
  metadata {
    disable_legacy_endpoints = true
  }
}