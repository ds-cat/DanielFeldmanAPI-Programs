#include <iterator>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

//import csv file stuff

std::vector<std::string> getNextLineAndSplitIntoTokens(std::istream& str)
{
    std::vector<std::string>   result;
    std::string                line;
    std::getline(str, line);

    std::stringstream          lineStream(line);
    std::string                cell;

    while (std::getline(lineStream, cell, ','))
    {
        result.push_back(cell);
    }
    // This checks for a trailing comma with no data after it.
    if (!lineStream && cell.empty())
    {
        // If there was a trailing comma then add an empty element.
        result.push_back("");
    }
    return result;
}


class CSVRow
{
public:
    std::string_view operator[](std::size_t index) const
    {
        return std::string_view(&m_line[m_data[index] + 1], m_data[index + 1] - (m_data[index] + 1));
    }
    std::size_t size() const
    {
        return m_data.size() - 1;
    }
    void readNextRow(std::istream& str)
    {
        std::getline(str, m_line);

        m_data.clear();
        m_data.emplace_back(-1);
        std::string::size_type pos = 0;
        while ((pos = m_line.find(',', pos)) != std::string::npos)
        {
            m_data.emplace_back(pos);
            ++pos;
        }
        // This checks for a trailing comma with no data after it.
        pos = m_line.size();
        m_data.emplace_back(pos);
    }
private:
    std::string         m_line;
    std::vector<int>    m_data;
};

std::istream& operator>>(std::istream& str, CSVRow& data)
{
    data.readNextRow(str);
    return str;
}

class CSVIterator
{
public:
    typedef std::input_iterator_tag     iterator_category;
    typedef CSVRow                      value_type;
    typedef std::size_t                 difference_type;
    typedef CSVRow* pointer;
    typedef CSVRow& reference;

    CSVIterator(std::istream& str) :m_str(str.good() ? &str : nullptr) { ++(*this); }
    CSVIterator() :m_str(nullptr) {}

    // Pre Increment
    CSVIterator& operator++() { if (m_str) { if (!((*m_str) >> m_row)) { m_str = nullptr; } }return *this; }
    // Post increment
    CSVIterator operator++(int) { CSVIterator    tmp(*this); ++(*this); return tmp; }
    CSVRow const& operator*()   const { return m_row; }
    CSVRow const* operator->()  const { return &m_row; }

    bool operator==(CSVIterator const& rhs) { return ((this == &rhs) || ((this->m_str == nullptr) && (rhs.m_str == nullptr))); }
    bool operator!=(CSVIterator const& rhs) { return !((*this) == rhs); }
private:
    std::istream* m_str;
    CSVRow              m_row;
};


class CSVRange
{
    std::istream& stream;
public:
    CSVRange(std::istream& str)
        : stream(str)
    {}
    CSVIterator begin() const { return CSVIterator{ stream }; }
    CSVIterator end()   const { return CSVIterator{}; }
};

//end of csv file import classes

int main()
{
    
    std::ifstream file("IMDB_Altered.csv");//import csv file
    ofstream processed_data;//file for data after processing
    processed_data.open("IMDB_Processed.csv");//open file
    processed_data << "review,dataset orignal sentiment, api 1 sentiment, api 2 sentiment, api 3 sentiment" << endl;//make first line always header
    vector<string> reviews;//review holding in memory
    vector<string> datasetOG;//og sentiment holding in memory
    vector<string> api1Results;//api 1 Results holding in memory
    vector<string> api2Results;//api 2 Results holding in memory
    vector<string> api3Results;//api 3 Results holding in memory

    int i = 0;
    for (auto& row : CSVRange(file))//for each row in csv file
    {   
        if (i < 2002)//only want the first 2000 points of data
        {
            //std::cout << "review " << i <<": " << row[1] << "\n";//print data
            if (i > 0)
            {
               // reviews.push_back(string(row[0]));
               // datasetOG.push_back(string(row[1]));
            }
            ++i;
        }
    }
    //write reviews into textfile
   // ofstream datafile;
   // datafile.open("dataset_results.txt");
   // i = 0;
  //  while (i < datasetOG.size())
   // {
    //    datafile << datasetOG.at(i) << endl;
    //    ++i;
   // }

}