output "ecr_repository_backend_url" {
  value = aws_ecr_repository.app_backend_repo.repository_url
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.app_cluster.name
}

output "ecs_service_name" {
  value = aws_ecs_service.app_service.name
}

output "ecs_task_definition_name" {
  value = aws_ecs_task_definition.app_task.family
}

output "alb_dns_name" {
  value = aws_lb.app_alb.dns_name
}
