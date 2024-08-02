import setuptools_scm
setuptools_scm.version
how_to_version = '''
all release version must be tagged on master
the develop branch version must tagged as vx.x.x.dev
if we see vx.x.x.post1.dev1 that means we are missing some tags
'''
print(how_to_version)
print(setuptools_scm.get_version(
        version_scheme="guess-next-dev",
        local_scheme="node-and-timestamp"
))
