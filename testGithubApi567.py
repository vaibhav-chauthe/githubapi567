import unittest 
import json
from unittest.mock import Mock, patch
from GitHubApi567 import gImpl as u1
from githubClient import gCL as repo_Call

class TestFetchUserDetailsService(unittest.TestCase):
    def test_fetch_user_repos(self):
        self.assertEqual(len(u1().fetchUserRepos('vaibhav-chauthe')),4)
        print('testFetchUserRepos successful')

    def test_fetch_user_repos_blank_value(self):
        with self.assertRaises(ValueError):
            u1().fetchUserRepos(' ')
        print('testFetchUserReposBlankValue successful')

    #Mock fetch user api
    @patch.object(repo_Call, "fetch_user_repo")
    def test_fetch_user_repo_mock_api(self, mock_fetch_user_repo):
        response_file = open('./json/response_fetch_user_repo.json')        
        repo_call_response = json.load(response_file)
        mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value = json.loads(json.dumps(repo_call_response))
        response = repo_Call.fetch_user_repo('vaibhav-chauthe')
        #print(response)
        self.assertEqual(response[0]['name'],"githubapi567")
        response_file.close()

    #Mock fetch commit api
    @patch.object(repo_Call, "fetch_repo_commits")
    def test_fetch_repo_commits_mock_api(self, mock_fetch_user_repo):
        response_file = open('./json/response_fetch_repo_commits.json')        
        repo_call_response = json.load(response_file)
        mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value = json.loads(json.dumps(repo_call_response))
        response = repo_Call.fetch_repo_commits('vaibhav-chauthe', ['githubapi567'])
        #print(response)
        self.assertEqual(len(response),12)
        response_file.close()

if __name__ == "__main__":
    unittest.main()