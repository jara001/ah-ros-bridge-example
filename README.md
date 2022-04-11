# ah_ros_bridge_example
Example of a ROS connector for Arrowhead Framework.


## Requirements
- `autopsy >= 0.4.1`, download [here](https://github.com/jara001/autopsy)
- `aclpy >= 0.2.0`, download [here](https://github.com/jara001/ah-acl-py)
- `websocket-client`, download using `python3 -m pip install websocket-client`


## Example configuration
_Note: This is currently stored inside `./ah_ros_bridge_example/module/configuration.py`._

```python
Server = ArrowheadServer(
    address = "127.0.0.1",
)

Interface = ArrowheadInterface(
    name = "HTTP-INSECURE-JSON",
)

Service = ArrowheadService(
    name = "echo",
)

Client = ArrowheadClient(
    name = "ros-machine",
    address = "192.168.1.1",
    port = 0,
    pubfile = "/home/machine/keys/ros-machine.pub",
    p12file = "/home/machine/keys/ros-machine.p12",
    p12pass = "abcd",
    cafile = "/home/machine/keys/cloud.ca",
    server = Server,
    interfaces = [Interface],
)
```