import csv
import matplotlib.pyplot as plt


def load_github_data():
    with open('issues.csv') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        issues = list(csv_reader)
    with open('repos.csv') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        repos = list(csv_reader)
    return repos, issues

######################### TASK 1 #########################
def plot_top_10_languages_repo_stat(repos):
    """
    Generate one plot with two subplots side by side
    Left subplot: a horizontal bar chart. The y axis is the coding languages, and the x axis is total repository number which coded in this lanaguage.
    Right subplot: a bar chart. Each portion is a coding lanaguage.

    Args:
        repos (List[List]): a list of lists. Each item contains: coding lanaguage, total repo number
        Example: [['Python', 548870], ['Java', 369282], ['C++', 278066], ...]
    """
    
    colors = ["#e8d8e0","#aebbdb","#dbc4bc","#ecd8d7","#f4a29d",
              "#cad69e","#cbaedb","#d6bf9f","#b4cbe9","#ece6a2"]
    
    # TODO: implement this function
    top_10 = sorted(repos, key=lambda x: x[1], reverse=True)[:10]
    
    languages = [item[0] for item in top_10]
    repo_counts = [item[1] for item in top_10]
    
    colors = ["#e8d8e0","#aebbdb","#dbc4bc","#ecd8d7","#f4a29d",
              "#cad69e","#cbaedb","#d6bf9f","#b4cbe9","#ece6a2"]
    
    fig, axs = plt.subplots(1, 2, figsize=(15, 7))
    
    axs[0].barh(languages, repo_counts, color=colors)
    axs[0].set_title('Top 10 Languages by Repository Count')
    axs[0].set_xlabel('Number of Repositories')
    axs[0].invert_yaxis()
    
    axs[1].pie(repo_counts, labels=languages, autopct='%1.1f%%', startangle=140, colors=colors)
    axs[1].set_title('Top 10 Languages Proportion')
    
    plt.tight_layout()
    plt.show()

######################### TASK 2 #########################
def plot_issue_trend_by_language(issues, languages=['Python', 'C', 'C++', 'Java', 'JavaScript', 'HTML']):
    """
    Generate a multi-line chart. The x axis is the year, and the y axis is the number of issues. Each line represents a coding language.

    Args:
        issues (List[List]): a list of lists, each list item contains: coding language name, year, quarter, count
        Example: [['Python', '2012', '1', '6774'], ['Java', '2012', '1', '4429'], ['C++', '2012', '1', '3421']...]
        Here ['Python', '2012', '1', '6774'] means 6774 issues are found in Python repos in the first quarter of year 2012

        languages (List[Str]): a list of coding language names

    Tips:
        1. create a nested dictionay with following data structure would be helpful:
            {
                "Python": {
                    "2012": 78383, # this is the sum of 4 quarters
                    "2013": 176586,
                    ...
                },
                "Java": {
                    "2012": 49331,
                    "2013": 146833,
                    ...
                },
                ...
            }
        2. the total count of a year is the sum of each quarter
    """

    colorDict = {
        'Python': '#cbaedb', 
        'C':'#aebbdb', 
        'C++':'#dbc4bc', 
        'Java':'#aed6c1', 
        'JavaScript':'#f4a29d', 
        'HTML':'#cad69e'
    }

    # TODO: implement this function
    trends = {}
    
    for lang in languages:
        trends[lang] = {}
    
    for lang, year, _, count in issues:
        if lang in languages:
            if year not in trends[lang]:
                trends[lang][year] = 0
            trends[lang][year] += int(count)
    
    plt.figure(figsize=(12, 8))
    
    for lang in languages:
        years = sorted(trends[lang].keys())
        counts = [trends[lang][year] for year in years]
        plt.plot(years, counts, label=lang)
    
    plt.title('GitHub Issue Trends by Language')
    plt.xlabel('Year')
    plt.ylabel('Number of Issues')
    plt.legend(title='Language')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    repos, issues = load_github_data()
    repos = [[repo[0], int(repo[1])] for repo in repos]
    plot_top_10_languages_repo_stat(repos)
    plot_issue_trend_by_language(issues)


if __name__ == '__main__':
    main()
