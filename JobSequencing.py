def job_sequencing(jobs):
	# Sort the jobs in descending order according to their profit
	jobs.sort(key = lambda x:x[2], reverse = True)
	
	# Find the maximum deadline among the jobs
	max_deadline = max(jobs, key = lambda x:x[1])[1]
	
	#create a list to store the job sequence
	sequence = [None] * max_deadline
	
	#create a count to store job count
	job_count = 0
	
	#Iterate over the jobs and assign them to appropriate slots
	for job in jobs:
		deadline = job[1]-1 #converte deadline to zero-based index
		while deadline >= 0:
			if sequence[deadline] is None:
				sequence[deadline] = job[0] #Assign the job to slot
				job_count += 1
				break
			deadline -= 1
	# Remove the empty slots from the sequence
	sequence = [job for job in sequence if job is not None]
	return (sequence, job_count)


jobs = [(1,3,35),(2,4,30),(3,4,25),(4,2,20),(5,3,15),(6,1,12),(7,2,5)]
result = job_sequencing(jobs)
print("Job Sequence : ", result[0])
print("Job Count : ", result[1])
