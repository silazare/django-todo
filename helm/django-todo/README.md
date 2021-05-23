# django-todo

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![AppVersion: 1.0.0](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)

A Helm chart for django-todo demo application

**Homepage:** <https://github.com/shacker/django-todo>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.pullPolicy | string | `"Always"` |  |
| image.repository | string | `"exciter86/django-todo"` |  |
| image.restartPolicy | string | `"Always"` |  |
| image.tag | string | `"1.0"` |  |
| ingress.annotations | object | `{}` |  |
| ingress.create | bool | `true` |  |
| initImage.pullPolicy | string | `"Always"` |  |
| initImage.repository | string | `"postgres"` |  |
| initImage.tag | string | `"12.7-alpine"` |  |
| livenessProbe.failureThreshold | int | `6` |  |
| livenessProbe.initialDelaySeconds | int | `30` |  |
| livenessProbe.periodSeconds | int | `10` |  |
| livenessProbe.successThreshold | int | `1` |  |
| livenessProbe.timeoutSeconds | int | `5` |  |
| postgresqlDbName | string | `"postgres"` |  |
| postgresqlHost | string | `"postgres"` |  |
| postgresqlPassword | string | `"superpostgres"` |  |
| postgresqlPort | int | `5432` |  |
| postgresqlUser | string | `"postgres"` |  |
| readinessProbe.failureThreshold | int | `6` |  |
| readinessProbe.initialDelaySeconds | int | `30` |  |
| readinessProbe.periodSeconds | int | `10` |  |
| readinessProbe.successThreshold | int | `1` |  |
| readinessProbe.timeoutSeconds | int | `5` |  |
| replicaCount | int | `2` |  |
| resources.limits.cpu | string | `"200m"` |  |
| resources.limits.memory | string | `"500Mi"` |  |
| resources.requests.cpu | string | `"200m"` |  |
| resources.requests.memory | string | `"500Mi"` |  |
| secretKey | string | `"lksdf98wrhkjs88dsf8-324ksdm"` |  |
| service.port | int | `8000` |  |
| service.targetPort | int | `8000` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.create | bool | `true` |  |
