#include <iostream>
#include <queue>
#include <string>

using namespace std;

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

            return p1 > p2;
        }
};

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

int main(int argc, char * argv[])
{
    // read input file with python repo data line by line

    // preprocess each line for repo URL and percentage of python files in it

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