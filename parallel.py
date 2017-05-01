#!/usr/bin/env python

import jenkins
import time




# PARALLELIZATION BEGIN'S
print("PARALLELIZATION BEGIN'S")
server = jenkins.Jenkins('http://10.132.25.18:8080', username='user', password='user')
user = server.get_whoami()
print('HELLO %s FROM JENKINS' % (user['fullName']))



'''
### ASSIGN TO QUEUE AND BUILD
server.build_job('POC_1', {'PWD2': 'C:\IrdPyUtils'})
time.sleep(1)
queue_info_1 = server.get_queue_info()
while True:
    if queue_info_1:
        queue_info_1 = server.get_queue_info()
        queue_1 = queue_info_1[0].get('id')
        print "The first job is in the queue"
        break
    else:
        queue_info_1 = server.get_queue_info()
        print "Waiting for queue"
        
time.sleep(3)

builds_1 = server.get_running_builds()
running_builds_1 = str([ item['number'] for item in builds_1 ])[1:-1]
while True:
    if running_builds_1:
        builds_1 = server.get_running_builds()
        running_builds_1 = str([ item['number'] for item in builds_1 ])[1:-1]
        print "The first job is now building"
        break
    else:
        builds_1 = server.get_running_builds()
        running_builds_1 = str([ item['number'] for item in builds_1 ])[1:-1]
        time.sleep(1)




server.build_job('POC_2', {'PWD2': 'C:\IrdPyUtils'})
time.sleep(1)
queue_info_2 = server.get_queue_info()
while True:
    if queue_info_2:
        queue_info_2 = server.get_queue_info()
        queue_2 = queue_info_2[0].get('id')
        print "The second job is in the queue"
        break
    else:
        queue_info_2 = server.get_queue_info()
        print "Waiting for queue"
        
time.sleep(3)

builds_2 = server.get_running_builds()
running_builds_2 = str([ item['number'] for item in builds_2 ])[1:-1]
while True:
    if running_builds_2:
        builds_2 = server.get_running_builds()
        running_builds_2 = str([ item['number'] for item in builds_2 ])[1:-1]
        print "The second job is now building"
        break
    else:
        builds_2 = server.get_running_builds()
        running_builds_2 = str([ item['number'] for item in builds_2 ])[1:-1]
        time.sleep(1)




server.build_job('POC_3', {'PWD2': 'C:\IrdPyUtils'})
time.sleep(1)
queue_info_3 = server.get_queue_info()
while True:
    if queue_info_3:
        queue_info_3 = server.get_queue_info()
        queue_3 = queue_info_3[0].get('id')
        print "The third job is in the queue"
        break
    else:
        queue_info_3 = server.get_queue_info()
        print "Waiting for queue"
        
time.sleep(3)

builds_3 = server.get_running_builds()
running_builds_3 = str([ item['number'] for item in builds_3 ])[1:-1]
while True:
    if running_builds_3:
        builds_3 = server.get_running_builds()
        running_builds_3 = str([ item['number'] for item in builds_3 ])[1:-1]
        print "The third job is now building"
        break
    else:
        builds_3 = server.get_running_builds()
        running_builds_3 = str([ item['number'] for item in builds_3 ])[1:-1]
        time.sleep(1)



'''
# COLLECT CONSOLE OUTPUT
builds = server.get_running_builds()
running_builds = str([ item['number'] for item in builds ])[1:-1]
while True:
    if running_builds:
        time.sleep(1)
        builds = server.get_running_builds()
        running_builds = str([ item['number'] for item in builds ])[1:-1]
    else:
        
        print "CONSOLE OUTPUT BEGINS"
        builds = server.get_running_builds()
        running_builds = str([ item['number'] for item in builds ])[1:-1]
        
        print "CONSOLE OUTPUT FOR THE FIRST JOB"
        last_build_number = server.get_job_info('POC_1')['lastCompletedBuild']['number']
        console_1 = server.get_build_console_output('POC_1',last_build_number)

        print "CONSOLE OUTPUT FOR THE SECOND JOB"
        last_build_number = server.get_job_info('POC_2')['lastCompletedBuild']['number']
        console_2 = server.get_build_console_output('POC_2',last_build_number)

        print "CONSOLE OUTPUT FOR THE THIRD JOB"
        last_build_number = server.get_job_info('POC_3')['lastCompletedBuild']['number']
        console_3 = server.get_build_console_output('POC_3',last_build_number)
        file = console_1 + console_2 + console_3
        
        f = open('file.txt', 'w')
        f.write(file)
        f.close()
        
        print "CONSOLE OUTPUT ENDS"
        break




# PARALLELIZATION END'S
print("PARALLELIZATION END'S")
