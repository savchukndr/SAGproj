from git import Repo


class GitConnector:
    """
    Creates git object
    """

    def __init__(self, repo_dir, file_list, commit_message):
        self.file_list = [file_list]
        self.commit_message = commit_message
        self.repo = Repo(repo_dir)

    def repo_add(self):
        """Add file to git"""
        self.repo.index.add(self.file_list)

    def repo_commit(self):
        """Commit changes with commit message"""
        self.repo.index.commit(self.commit_message)

    def repo_push(self):
        """Push to git repo"""
        origin = self.repo.remote('origin')
        origin.push()


if __name__ == "__main__":
    git_conn = GitConnector('SAGrepo', 'testFile.txt', 'Commit Message')
    git_conn.repo_add()
    git_conn.repo_commit()
    git_conn.repo_push()