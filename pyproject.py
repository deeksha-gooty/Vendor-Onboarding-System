import random

class CloudResourceManager:
    MAX_MEMORY = 15 
    MEMORY_WARNING_THRESHOLD = 12

    def _init_(self):
        self.resources = []
        self.total_memory_allocated = 0
        self.default_memory = 5

    def generate_random_id(self):
        return str(random.randint(1000, 9999))

    def create_resource(self, name, resource_type):
        if self.total_memory_allocated + self.default_memory > self.MAX_MEMORY:
            print("Memory allocation exceeds the maximum limit. Resource creation failed.")
            return None

        resource_id = self.generate_random_id()
        print(resource_id,"THIS IS YOUR ID")
        resource_key = f"{name}{resource_type}{resource_id}"
        resource = {'id': resource_id, 'name': name, 'type': resource_type, 'memory': self.default_memory, 'key': resource_key}
        self.resources.append(resource)
        self.total_memory_allocated += self.default_memory

        if self.total_memory_allocated >= self.MEMORY_WARNING_THRESHOLD:
            print("Warning: Total memory usage is near the limit.")
    
        return resource

    def read_resource(self, ID):
        resource_id = ID
    
        resource_found = False
        for resource in self.resources:
            if resource['id'] == resource_id:
                resource_found = True
                break

        if not resource_found:
            print("Resource with the specified ID does not exist.")
            return None

        print("{",resource_id,":{ Resource Name:",resource['name'],", Resource Type:",resource['type'],", Memory:",resource['memory'],"} }")
        return None



    def update_resource(self, resource_id, new_name, new_id, new_memory):
        found=False
        for resource in self.resources:
            if resource['id'] == resource_id:
                resource['name'] = new_name
                self.default_memory = self.default_memory + new_memory
                if self.default_memory <= self.MAX_MEMORY:
                    resource['memory'] = self.default_memory
                    if self.default_memory >= self.MEMORY_WARNING_THRESHOLD:
                        print("Warning: Total memory usage is near the limit.")
                    resource['id'] = new_id
                    found=True
                    return resource
                else:
                    print("Alert:Memory allocation exceeds the maximum limit.")
        if found==False:
            print("Invalid Resource ID")

    def monitor_resource_usage(self, resource_id):
        for resource in self.resources:
            if resource['id'] == resource_id:
                print("Resource Usage Details:")
                print("ID:", resource['id'])
                print("Name:", resource['name'])
                print("Type:", resource['type'])
                print("Memory Allocated:", resource['memory'])
                print("Key:", resource['key'])
                return None

        print("Resource with the specified ID does not exist.")
        return None

        
    def delete_resource(self, resource_id):
        for index, resource in enumerate(self.resources):
            if resource['id'] == resource_id:
                self.total_memory_allocated -= resource['memory']
                deleted_resource = self.resources.pop(index)

                if self.total_memory_allocated >= self.MEMORY_WARNING_THRESHOLD:
                    print("Warning: Total memory usage is near the limit.")

                return deleted_resource
        return None

    def list_resources(self):
        return self.resources

def main():
    cloud_manager=CloudResourceManager()

    while True:
        print("\nOptions:")
        print("1. Create Resource")
        print("2. Read Memory Allocated for Resource")
        print("3. Update Resource")
        print("4. memory resource usage")
        print("5. Delete Resource")
        print("6. List Resources")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter resource name: ")
            resource_type = input("Enter resource type: ")
            cloud_manager.create_resource(name, resource_type)
        
        elif choice == '2':
            id = input("Enter resource ID to read: ")
            result = cloud_manager.read_resource(id)
            if result is not None:
                 print("Resource Details\n", result)
                 
        elif choice == '3':
            resource_id = input("Enter resource ID to update: ")
            new_name = input("Enter new name for the resource: ")
            new_memory = float(input("Enter new memory for the resource: "))
            new_id = str(random.randint(1000, 9999))
            result = cloud_manager.update_resource(resource_id, new_name, new_id, new_memory)
            if result is not None:
                print("Updated Resource:", result)

        elif choice == '4':
            resource_id = input("Enter resource ID to monitor: ")
            cloud_manager.monitor_resource_usage(resource_id)


        elif choice == '5':
            resource_id = input("Enter resource ID to delete: ")
            result = cloud_manager.delete_resource(resource_id)
            if result is not None:
                print("Deleted Resource:", result)
            else:
                print(f"Resource with ID {resource_id} not found.")

        elif choice == '6':
            t = cloud_manager.list_resources()
            if len(t)!=0:
                print("List of Resources:")
                print("{ ",end=' ')
                for i in range(len(t)-1):
                    print(t[i]['id'],"{ Name: ",t[i]['name'],", Type: ",t[i]['type'],", Memory: ",t[i]['memory'],", Key: ",t[i]['key']," }")
                print(t[len(t)-1]['id'],"{ Name: ",t[len(t)-1]['name'],", Type: ",t[len(t)-1]['type'],", Memory: ",t[len(t)-1]['memory'],", Key: ",t[len(t)-1]['key']," }"," }")
            else:
                print(f"Resource is empty.")
        
        elif choice == '7':
            print("Exiting Cloud Resource Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
