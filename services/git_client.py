from git import Repo
import os, shutil

_repo = None

def clean_tmp_dir():
    folder = './tmp/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def clone_repo(repo_ur : str):
    clean_tmp_dir()
    Repo.clone_from(repo_ur, "./tmp/")


def commit_ci_file():
    _repo = Repo('./tmp/')
    _repo.index.add(['.gitlab-ci.yml'])
    if _repo.is_dirty(untracked_files=True):
        print('Changes detected.')
        _repo.index.commit('Update CI_CD')
        print(_repo.remotes.origin.push())

# getRepo("c")
commit_ci_file()
