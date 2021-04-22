
import os


server = jenkins.Jenkins('http://localhost:8080', username='aqeel', password='1150f04cbd7f975e0ace403088389dc7af')
last_build_number = server.get_job_info('FAKT_Job')['builds'][0]['number']
build_info = server.get_build_info('FAKT_Job', last_build_number)['actions'][0]['parameters'][0]['value']
jobs_address = '/Users/aqeel/fakt_remote/' + str(build_info)
for filename in os.listdir(jobs_address):
    print(filename)
