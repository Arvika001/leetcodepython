class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        // Create a vector of pairs (height, name)
        vector<pair<int, string>> people;
        
        // Populate the people vector
        for (int i = 0; i < names.size(); i++) {
            people.emplace_back(heights[i], names[i]);
        }
        
        // Sort the people vector in descending order based on height
        sort(people.begin(), people.end(), [](const pair<int, string>& a, const pair<int, string>& b) {
            return a.first > b.first;
        });
        
        // Extract the sorted names
        vector<string> sortedNames;
        for (const auto& person : people) {
            sortedNames.push_back(person.second);
        }
        
        return sortedNames;
    }
};
