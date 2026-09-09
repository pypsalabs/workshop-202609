# Single-user server runs as root under the Elestio DockerSpawner (user=0).
c.ServerApp.allow_root = True

# Cull idle kernels after 30 min, even with the tab open, so morning kernels free memory over lunch.
c.MappingKernelManager.cull_idle_timeout = 1800
c.MappingKernelManager.cull_interval = 300
c.MappingKernelManager.cull_connected = True
