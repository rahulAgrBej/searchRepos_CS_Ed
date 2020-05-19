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
        double pythonPercentage;

    public:

        repoURL(string urlIn, double percentIn);
};


int main(int argc, char * argv[])
{
    // read input file with python repo data line by line

    // preprocess each line for repo URL and percentage of python files in it

    // push preprocessed repo data to priority to sort URLS based off of highest percentage first

    return 0;
}

// returns a priority queue
priority_queue<string> buildPQ()
{
    priority_queue<string> pq;

    return pq;
}