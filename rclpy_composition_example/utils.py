import os
import inspect
import ament_index_python as ament_index


def register_component(type_str, node_cls):
    resource_path = ""
    for p in ament_index.get_search_paths():
        if p.find("/opt/ros/"):
            resource_path = p

    res_name, cls_name = str.split(type_str, '::')

    source_code = inspect.getsource(node_cls)
    res_file_relative_path = "lib/lib" + str.lower(cls_name) + ".py"
    res_file_path = os.path.join(resource_path, res_file_relative_path)
    with open(res_file_path, "w") as f:
        print('writing', source_code)
        print('to', res_file_path)
        f.write(source_code)

    res_folder = os.path.join(resource_path, "share/ament_index/resource_index/rclpy_components/")
    if not os.path.exists(res_folder):
        os.mkdir(res_folder)
    res_path = os.path.join(res_folder, res_name)
    with open(res_path, 'w') as f:
        content = '{};{}'.format(type_str, res_file_relative_path)
        print('writing' ,content)
        print('to', res_path)
        f.write(content)

def register_component_in_setuppy(package_name, rclpy_components):
    """

    :param rclpy_components: A list of setuptool entrypoint strings,
        like ['composition::Talker=rclpy_components_examples:Talker']
    :return: None
    """

    resource_path = ""
    print('search_paths:', ament_index.get_search_paths())
    for p in ament_index.get_search_paths():
        if package_name in p:
            resource_path = p

    # Parse the entry points
    resources = {} # Key: resource_name, value: list of resource strings
    for rclpy_component_str in rclpy_components:
        parts = str.split(rclpy_component_str, '=')
        resource_str = parts[0].strip() # In the pattern 'RES_NAME::RES_CLASS'
        resource_name = str.split(resource_str, '::')[0]
        entry_point_path = parts[1].strip()

        content = '{};{}'.format(resource_str, entry_point_path)
        if resource_name in resources:
            resources[resource_name].append(content)
        else:
            resources[resource_name] = [content]

    res_folder = os.path.join(resource_path, "share/ament_index/resource_index/rclpy_components/")
    if not os.path.exists(res_folder):
        os.mkdir(res_folder)

    for resource_name, contents in resources.items():
        res_path = os.path.join(res_folder, resource_name)
        with open(res_path, 'w') as f:
            f.writelines(contents)
