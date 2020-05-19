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

    if (argc != 2)
    {
        cout << "Please include a filepath!" << endl;
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

        repoURL repo(gitRepo, percent);
        repoPQ.push(repo);
    }

    cout << "TESTING PQ" << endl;
    cout << repoPQ.top().getURL() << endl;
    cout << repoPQ.top().getPyPercent() << endl;
    cout << "size: " << repoPQ.size() << endl;

    repoPQ.pop();
    cout << "size: " << repoPQ.size() << endl;
    cout << repoPQ.top().getURL() << endl;
    cout <<"percent " << repoPQ.top().getPyPercent() << endl;
    cout << "size: " << repoPQ.size() << endl;

    repoPQ.pop();
    cout << "size: " << repoPQ.size() << endl;

    // push preprocessed repo data to priority to sort URLS based off of highest percentage first

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

// returns a priority queue
priority_queue<string> buildPQ()
{
    priority_queue<string> pq;

    return pq;
}