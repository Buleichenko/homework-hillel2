def process_file_permissions():
    num_files = int(input())
    file_permissions = {}

    for _ in range(num_files):
        file, *permissions = input().split()
        file_permissions[file] = permissions

    num_queries = int(input())

    for _ in range(num_queries):
        operation, file = input().split()
        if operation in file_permissions.get(file, []):
            print("OK")
        else:
            print("Access denied")


process_file_permissions()
