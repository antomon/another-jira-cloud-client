from jira import JIRA







if __name__ == '__main__':


    user = 'amontano@altaformazione.it'
    apikey = 'oE33uTqsFMBvMVbkguPE214C'
    server = 'https://altaformazione.atlassian.net/'

    options = {
        'server': server
    }

    jira = JIRA(options, basic_auth=(user, apikey))

    issues = jira.search_issues("project = DPD1",
                                startAt=0,
                                maxResults=50,
                                validate_query=True,
                                fields=["issuetype", "status", "summary"],
                                expand=None,
                                json_result=None)

    row = 1
    col = 1
    workbook = xlsxwriter.Workbook('jira-excel.xlsx')
    header = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#D8E4BC'})
    center = workbook.add_format({'align': 'center'})
    worksheet = workbook.add_worksheet('Summary')
    worksheet.write(row, col, 'Issue Type', header)
    worksheet.write(row, col + 1, 'Count', header)
    row += 1
    for index, dat in df.iterrows():
        worksheet.write(row + index, col, dat['issuetype'])
        worksheet.write(row + index, col + 1, int(dat['count']), center)
    workbook.close()

    for project in jira.projects():
        print(project.key)
        print(project.raw)

        issues_in_proj = jira.search_issues('project=' + project.key, maxResults=1000)

        for issue in issues_in_proj:
            print('{} - {}: {}'.format(issue.fields.issuetype.name, issue.key, issue.fields.summary))
            print(issue.raw)

            issue_worlogs = jira.worklogs(issue.key)
            if len(issue_worlogs) > 0:
                print(issue_worlogs)
                for issue_worlog in issue_worlogs:
                    issue_worlog.author, issue_worlog.emailAddress
                    print(issue_worlog.raw)
                    issue_worlog.timeSpent, issue_worlog.timeSpentSeconds, issue_worlog.started

