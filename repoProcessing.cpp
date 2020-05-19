#include <iostream>
#include <queue>
#include <string>

using namespace std;

// comparator to sort URLs
// highest percentage of files that are written in python are favoured
class pyPercentCompare
{

};

// class for repoURLs
class repoURL
{
    private:

        string url;
        double pyPercent;

    public:

        repoURL(string urlIn, double percentIn);
        string getURL();
        double getPyPercent();
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
string repoURL::getURL()
{
    return url;
}

// getter function - returns pyPercent
double repoURL::getPyPercent()
{
    return pyPercent;
}

// returns a priority queue
priority_queue<string> buildPQ()
{
    priority_queue<string> pq;

    return pq;
}