from GitConnector import GitConnector

with (open("/Users/savchuk/PycharmProjects/SAGproj/SAGrepo/testFile.txt", 'w')) as fl:
    fl.write("string 2\n")
    fl.close()


git_conn = GitConnector('SAGrepo', 'testFile.txt', 'Commit String 2')
git_conn.repo_add()
git_conn.repo_commit()
git_conn.repo_push()