import requests
import json



if __name__ == '__main__':
    try:
        response = requests.get('http://localhost:8000/api/projects')
        projects = ""
        print(' ---------------- Get project list ---------------- ')
        if response.status_code == 200:
            projects = json.loads(response.text)
        print(f" ----- Number of elements :  {len(projects)}")
        print(' ----- First two Element : ')
        print(json.dumps(projects[0:2], indent=4))
        print(' ---------------- END Get project list ---------------- \n')

        next_response = requests.get('http://localhost:8000/api/projects/first-test-project')
        print(' ---------------- Get Single project by SLUG  ---------------- ')
        single_project = ""
        if next_response.status_code == 200:
            single_project = json.loads(next_response.text)
        print(' ----- Slug used by the request : first-test-project')
        print(' ----- Element : ')
        print(json.dumps(single_project, indent=4))
        print(' ---------------- END Get Single project by SLUG  ---------------- \n')

    except Exception as e:
        raise e