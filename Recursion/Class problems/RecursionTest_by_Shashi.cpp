/////////// Problem 1 ////////////////

// Brute Force

// Time - 2^n * n + 2^n * n
// Space - 2^n * n + O(n)
result[][];

void helper(arr[], i, slate)
{
    if (i == arr.size())
    {
        result.add(slate); // O(n)
        return;
    }

    helper(arr, i + 1, slate); // exclude

    slate.add(arr[i]);         // write
    helper(arr, i + 1, slate); // include
    slate.pop_back();          // erase
}

bool overall(arr[], k)
{
    helper(arr, 0, []); // generate all the posiible subsets
    /*

    iterate in result list to check do we have any non-empty subset 
    having sum ==k. 
    and then return true or false.

    */
}

//////////////////////////////////

// optimized Approach

// Time - O(2 ^ n)
//Space - O(n) +   O(n)  + O(1)

bool helper(arr[], i, k, sum, size)
{

    if (sum == k) // backTracking case
    {
        if (size >= 1)
            return true;
    }
    if (i == arr.size()) // Base case
        return false;

    if (helper(arr, i + 1, k, sum, size) == true) // excluding
        return true;

    return helper(arr, i + 1, k, sum + arr[i], size + 1); // including

    // return (helper(arr, i + 1, k, sum, size) || helper(arr, i + 1, k, sum + arr[i], size + 1) );
}

bool overall(arr[], k)
{
    return helper(arr, 0, k, 0, 0);
}

//////////////////////

//////////////// Problem 2 ///////////

// -> Brute Force Approach
// ( - opening
// ) - closing
// ((()))
bool is_well_formed(string s) // O(2n)
{
    int open = 0;
    int close = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == '(')
            open++;
        else
            close++;
        if (close > open)
            return false;
    }
    return (open == close);
}

result[];

void helper(int n, int i, slate)
{
    if (i == n)
    {
        result.add(slate); // O(2n)
        return;
    }

    slate = slate + '('; // open
    helper(n, i + 1, slate);
    slate.pop_back();

    slate = slate + ')'; // close
    helper(n, i + 1, slate);
    slate.pop_back();
}

// O(2^l) == O(2^2n )

// Time - O(2^2n * 2n) + O(2^2n * 2n) =  O(2^2n * 2n)
//Space - O(1) +   O(2^2n * 2n) + O(2n)   + O(2^2n * 2n)

list<string> generateParenthesis(int n)
{
    helper(2 * n, 0, ""); // O(2^2n * 2n)
    list<string> ans;

    for (int i = 0; i < result.size(); i++) // O(2^2n * 2n)
    {
        if (is_well_formed(result[i])) // O(2n)
        {
            ans.add(result[i]);
        }
    }
    return ans;
}
// optimized Approach

result[]; // valid brackets

void helper(int n, int open, int close, slate)
{

    if (open > n || close > n || close > open) // backtracking
        return;

    if (open == close == n) // Base
    {
        result.add(slate); // O(2n)
        return;
    }

    slate = slate + '('; // open
    helper(n, open + 1, close, slate);
    slate.pop_back();

    slate = slate + ')'; // close
    helper(n, open, close + 1, slate);
    slate.pop_back();
}

list<string> overall(int n)
{

    helper(n, 0, 0, "");
    return result;
}