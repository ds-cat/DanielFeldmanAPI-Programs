#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include<numeric>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <chrono>
#include <thread>
#include <random>



using namespace std;
using namespace std::chrono;


int sample_size=50;
int run_size=50;

vector<int> cluster_sizes;
vector<int> cluster_temp;
vector<int>  cluster_pro;
int n = 0;
int max_cluster = 0;
int temp;
int templist;
vector<int> ids;

string k = "-3";
string inputfilename = "clustered_sentances" + k + ".csv";

void Cluster_Prop_Assign(string filename)
{
	string line;
	string word;
	vector<string>row;
	vector<vector<string>>content;
	//read in csv
	fstream file(filename, ios::in);
	if (file.is_open())
	{
		while (getline(file, line))
		{
			row.clear();

			stringstream str(line);

			while (getline(str, word, ','))
				row.push_back(word);
			content.push_back(row);
		}
	}
	else
		cout << "Could not open the file\n";
	for (int i = 0; i < content.size(); i++)
	{
		for (int j = 0; j < content[i].size()-1; j++)
		{
			if(i%2 == 1)
				if (stoi(content[i][j + 1]) > max_cluster)
				{
					max_cluster = stoi(content[i][j + 1]);
				}
				cluster_temp.push_back(stoi(content[i][j+1]));
		}
		
	}
	for (int i = 0; i <= max_cluster; ++i)
	{
		cluster_sizes.push_back(count(cluster_temp.begin(), cluster_temp.end(), i));
	}

}
uint64_t timeSinceEpochMillisec() {
	using namespace std::chrono;
	return duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
}



vector<int>  Cluster_Samples_ID(vector<int>sizes, vector<int>temp, float sample)
{
	vector<int>id;
	int randhold;
	float prop = sample / 2000;
	transform(sizes.begin(), sizes.end(), sizes.begin(), [prop](int& c) { return c * prop; });
	while (accumulate(sizes.begin(), sizes.end(), 0)< sample)
	{
		std::random_device rd;  //Will be used to obtain a seed for the random number engine
		std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
		std::uniform_int_distribution<> distrib(0, max_cluster);
		//cout << distrib(gen) << endl;
		++sizes.at(distrib(gen));
	}
	int zed = 0;
	//cout << accumulate(sizes.begin(), sizes.end(), 0) << endl;
	while (accumulate(sizes.begin(), sizes.end(),0) >0)
	{
		std::random_device rd;  //Will be used to obtain a seed for the random number engine
		std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
		std::uniform_int_distribution<> distrib2000(0, 2000);
		randhold = distrib2000(gen);
		//cout << randhold << endl;
		if (count(id.begin(), id.end(), randhold) == 0)
		{
			if (randhold <= 1999 && randhold >=0)
			{
				zed = sizes.at(temp.at(randhold));
				if (zed > 0)
				{

					id.push_back(randhold);
					//cout << sizes.at(temp.at(randhold)) << endl;
					sizes.at(temp.at(randhold)) = sizes.at(temp.at(randhold)) - 1;
					//cout << sizes.at(temp.at(randhold)) << endl;
					//cout << accumulate(sizes.begin(), sizes.end(), 0) << endl;
				}
				else
				{
					//cout << "ding " << endl;
				}
			}
		}
		//cout << zed << endl;
		
		//cout << accumulate(sizes.begin(), sizes.end(), 0) <<endl;
	}
	//out << accumulate(sizes.begin(), sizes.end(), 0);
	return id;
}



void API_acc(vector<int> id, float &one, float &two, float &three)
{
	//text,dataset,fyhao api,twinword api,symanto api
	vector<string> stringtemp;
	string line;
	string word;
	vector<string>row;
	vector<vector<string>>content;
	//read in csv
	fstream file("dataset_results.csv", ios::in);
	if (file.is_open())
	{
		int x = 0;
		int fixer = 0;
		while (getline(file, line))
		{
			
			row.clear();
			//cout << line << endl;
			stringstream str(line);
			
			while (getline(str, word, ','))
			{
				++x;
				//cout << word << endl;
				word.erase(remove(word.begin(), word.end(), '"'), word.end());
				word.erase(remove(word.begin(), word.end(), '\n'), word.cend());
				if (word != "")
				{
					//cout << word << endl;
					if (fixer < 5)
					{
						
						stringtemp.push_back(word);
						++fixer;
					}
					else
					{
						content.push_back(stringtemp);
						stringtemp.clear();
						stringtemp.push_back(word);
						fixer = 1;
					}
				}
				if (content.size() == 1999)
				{
					if (stringtemp.size() == 5)
					{
						content.push_back(stringtemp);
					}
				}
				
			}
			
			
				
		}
		//cout << content.at(1999).at(0) << endl;
	}
	else
		cout << "Could not open dataset results\n";
	for (int i = 0; i < id.size(); ++i)
	{

		string GT;
		string check;
		
		
		GT = content.at(id.at(i)).at(1);
		check = content.at(id.at(i)).at(2);
		if (GT == check)
			++one;
		check = content.at(id.at(i)).at(3);
		if (GT == check)
			++two;
		check = content.at(id.at(i)).at(4);
		if (GT == check)
			++three;
	}
	int trueidsize = id.size() + 1;

	one = one / trueidsize;

	two = two / trueidsize;

	three = three / trueidsize;
}

vector<int> SRS_Samples_ID(int size)
{
	vector<int> temp;
	int i = 0;
	while ( i < size)
	{
		int randhold;
		std::random_device rd;  //Will be used to obtain a seed for the random number engine
		std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
		std::uniform_int_distribution<> distrib2000(0, 1999);
		randhold = distrib2000(gen);
		if ((count(temp.begin(), temp.end(), randhold))== 0)
		{
			temp.push_back(randhold);
			++i;
		}
	}
	return temp;


}
template<typename T>
double getAverage(std::vector<T> const& v) {
	if (v.empty()) {
		return 0;
	}
	return std::accumulate(v.begin(), v.end(), 0.0) / v.size();
}

int main()
{
	cout << "sample size:";
	cin >> sample_size;
	cout << "runs size:";
	cin >> run_size;

	vector<float> API_1_acc_avg;
	vector<float> API_2_acc_avg;
	vector<float> API_3_acc_avg;
	vector<float> API_1_SRS_avg;
	vector<float> API_2_SRS_avg;
	vector<float> API_3_SRS_avg;
	//get cluster proptions
	Cluster_Prop_Assign(inputfilename);
	

	//for each run size
	for (int i = 0; i < run_size; ++i)
	{
		float API_1_acc = 0;
		float API_2_acc = 0;
		float API_3_acc = 0;
		float SRS_1_acc = 0;
		float SRS_2_acc = 0;
		float SRS_3_acc = 0;
		//get cluster samples
		ids = Cluster_Samples_ID(cluster_sizes, cluster_temp, sample_size);
		
		
		
		//get accuracy
		API_acc(ids, API_1_acc, API_2_acc, API_3_acc);
		API_1_acc_avg.push_back(API_1_acc);
		API_2_acc_avg.push_back(API_2_acc);
		API_3_acc_avg.push_back(API_3_acc);
		ids.clear();

		ids = SRS_Samples_ID(sample_size);

		//cout << ids.at(1);
		API_acc(ids, SRS_1_acc, SRS_2_acc, SRS_3_acc);
		API_1_SRS_avg.push_back(SRS_1_acc);
		API_2_SRS_avg.push_back(SRS_2_acc);
		API_3_SRS_avg.push_back(SRS_3_acc);
		cout << i << endl;
		ids.clear();
	}
	cout << abs(getAverage(API_1_acc_avg)- 0.584915084915084) << endl;
	cout << abs(getAverage(API_2_acc_avg)- 0.623376623376623)<< endl;
	cout << abs(getAverage(API_3_acc_avg) - 0.899600399600399)<< endl;
	
	cout << abs(getAverage(API_1_SRS_avg)- 0.584915084915084) << endl;
	cout << abs(getAverage(API_2_SRS_avg)- 0.623376623376623)<< endl;
	cout << abs(getAverage(API_3_SRS_avg)- 0.899600399600399)<< endl;
}



