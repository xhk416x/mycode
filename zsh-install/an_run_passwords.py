import ansible_runner
import sys

# passw = {"sudo" : "alta3"}
# r= ansible_runner.run(playbook="/home/student/mycode/zsh-install/project/aptplaybook.yaml", private_data_dir=".", passwords=passw)
# print("{}: {}".format(r.status, r.rc))
out, err, rc = ansible_runner.run_command(
    executable_cmd='ansible-playbook',
    cmdline_args=['/home/student/mycode/zsh-install/project/aptplaybook.yaml', '-K'],
    input_fd=sys.stdin,
    output_fd=sys.stdout,
    error_fd=sys.stderr,
)
print("rc: {}".format(rc))
print("out: {}".format(out))
print("err: {}".format(err))