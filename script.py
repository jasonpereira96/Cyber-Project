from bs4 import BeautifulSoup
import json

dumpfile = "raw_data.txt"

with open(dumpfile) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
tuples = soup.findAll(type = "tuple")


jobs = []
print(len(tuples))
# print(tuples)
# change
# tuple1 = tuples[0]
# print(type(tuples[0]))
for tuple1 in tuples: 
    # print(tuple1)
    jobDetails = {}
    # title
    # title = tuple1.find(class_ = 'desig')['title']
    # jobDetails['title'] = title
    # desig
    desig = tuple1.find(class_ = 'desig').find('a').string
    jobDetails['desig'] = desig


    # url
    url = tuple1.find(class_ = 'desig').find('a')['href']
    jobDetails['url'] = url
    # org
    org = tuple1.find(class_ = 'org').string
    jobDetails['org'] = org

    # loc
    loc = tuple1.find(class_ = 'loc').find('span').string
    jobDetails['loc'] = loc

    # more desc
    # on hold
    # print(tuple1.find(class_ = 'more desc').)

    # exp
    exp = tuple1.find(class_ = 'exp', recursive=True)
    # print(exp)
    if exp is not None:
        # print(exp.contents[1])
        jobDetails['exp'] = exp.contents[1]

    # salary
    salary = tuple1.find(class_ = 'salary', recursive=True)
    if salary is not None:
        # print(str(salary.contents))
        print(salary.contents[-1])
        jobDetails['salary'] = str(salary.contents[-1])

    skill = tuple1.find(class_ = 'skill', recursive=True)
    if skill is not None:
        jobDetails['skillset'] = str(skill.contents[0])

    
        



    jobs.append(jobDetails)

# print(tuples[0].findAll(class_ = 'desig')[0].find('a').contents)
# print(tags[0].findAll(class_ = 'desig')[0].contents)

# print(json.dumps(jobs, sort_keys=True, indent=4))

with open('jobs.json', 'w') as fp:
    fp.write(json.dumps(jobs, sort_keys=True, indent=4))
