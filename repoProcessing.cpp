#include <iostream>
#include <queue>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

// class for repoURLs
class repoURL
{
    private:

        string url;
        double pyPercent;

    public:

        repoURL(string urlIn, double percentIn);
        string getURL() const;
        double getPyPercent() const;
};

// comparator to sort URLs
// highest percentage of files that are written in python are favoured
// ties are broken based off of url length, with priority to shorter URLs
class pyPercentCompare
{
    public:

        bool operator ()(const repoURL & repo1, const repoURL & repo2)
        {
            double p1 = repo1.getPyPercent();
            double p2 = repo2.getPyPercent();

            string url1 = repo1.getURL();
            string url2 = repo2.getURL();

            if (p1 == p2)
            {
                if (url1.length() == url2.length())
                { return true; }

                return url1.length() > url2.length();
            }

            return p1 < p2;
        }
};

int main(int argc, char * argv[])
{

    if (argc != 3)
    {
        cout << "Make sure to include inFile and outFile paths" << endl;
        return 0;
    }

    priority_queue<repoURL, vector<repoURL>, pyPercentCompare> repoPQ;

    // read input file with python repo data line by line
    ifstream inFile(argv[1]);

    // preprocess each line for repo URL and percentage of python files in it
    string line;
    getline(inFile, line);

    stringstream ssFirstLine;
    string token;
    ssFirstLine << line;
    ssFirstLine >> token;
    ssFirstLine >> token;
    int repoCount = 0;
    ssFirstLine >> repoCount;

    for (int i = 0; i < repoCount; ++i)
    {
        getline(inFile, line);
        stringstream ss(line);
        string token;

        // get repo name/path from first token
        ss >> token;
        string gitRepo = "NOT FOUND";
        string githubStr = "github.com/";
        string gitStr = ".git";
        size_t start = token.find(githubStr) + githubStr.length();
        size_t end = token.find(gitStr);

        if ((start != std::string::npos) && (end != std::string::npos))
        {
            gitRepo = token.substr(start, end-start);
        }

        // takes filler token
        ss >> token;

        double percent = 0.0;
        ss >> percent;

        // push preprocessed repo data to priority to sort URLS based off of highest percentage first
        repoURL repo(gitRepo, percent);
        repoPQ.push(repo);
    }

    // closes file
    inFile.close();

    // starts writing to result file
    ofstream outFile(argv[2], ofstream::out);

    for (int j = 0; j < repoCount; ++j)
    {
        outFile << repoPQ.top().getURL() << " " << repoPQ.top().getPyPercent() << endl;
        repoPQ.pop();
    }

    outFile.close();

    return 0;
}

// constructor for repoURL
repoURL::repoURL(string urlIn, double percentIn)
{
    url = urlIn;
    pyPercent = percentIn;
}

// getter function - returns string url
string repoURL::getURL() const
{
    return url;
}

// getter function - returns pyPercent
double repoURL::getPyPercent() const
{
    return pyPercent;
}