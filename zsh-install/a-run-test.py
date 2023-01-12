import ansible_runner as a_run
r = a_run.run(playbook="debplaybook.yaml", private_data_dir=".")
print("{}: {}".format(r.status, r.rc))
