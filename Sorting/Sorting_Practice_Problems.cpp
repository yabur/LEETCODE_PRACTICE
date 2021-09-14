
// https : //leetcode.com/problems/squares-of-a-sorted-array/
//// Implement Merge Sort

int aux[100000];

void merge(vector<int> &arr, int start, int mid, int end)
{
    int i = start;
    int j = mid + 1;
    int k = start;

    while (i <= mid && j <= end)
    {
        if (arr[i] <= arr[j])
        {
            aux[k] = arr[i];
            i++;
            k++;
        }
        else
        {
            aux[k] = arr[j];
            j++;
            k++;
        }
    }

    while (i <= mid)
    {
        aux[k] = arr[i];
        i++;
        k++;
    }

    while (j <= end)
    {
        aux[k] = arr[j];
        j++;
        k++;
    }

    for (int x = start; x <= end; x++)
    {
        arr[x] = aux[x];
    }
}

void helper(vector<int> &arr, int start, int end) // merge_sort_rec
{
    if (start >= end)
        return;

    int mid = (start + end) / 2;
    helper(arr, start, mid);
    helper(arr, mid + 1, end);

    merge(arr, start, mid, end);
}

vector<int> merge_sort(vector<int> &arr)
{
    int n = arr.size();

    helper(arr, 0, n - 1);

    return arr;
}

///////
/*
 * Complete the merger_first_into_second function below.
 */

// Time - O(m+n), Space -  O(1)
void merger_first_into_second(vector<int> &arr1, vector<int> &arr2)
{

    int n = arr1.size();

    int i = n - 1; //
    int j = n - 1;
    int k = (2 * n) - 1;

    while (i >= 0 && j >= 0) // 1=2 -- i=-1
    {
        if (arr1[i] >= arr2[j])
        {
            arr2[k] = arr1[i];
            k--;
            i--;
        }
        else
        {
            arr2[k] = arr2[j];
            k--;
            j--;
        }
    }

    while (i >= 0)
    {
        arr2[k] = arr1[i];
        k--;
        i--;
    }

    // this is not required
    while (j >= 0)
    {
        arr2[k] = arr2[j];
        k--;
        j--;
    }
}

/////////

/// Group the Numbers
// Lomuto's partition
// Time - O(n), Space -O(1)
vector<int> solve(vector<int> arr)
{
    int n = arr.size();

    int even = -1; // r -- red == even
    int i = 0;     // current pointer
    while (i < n)  /// O(n)
    {
        if (arr[i] % 2 == 0) // even - red
        {
            even++;                  // r++
            swap(arr[i], arr[even]); // O(1)
        }
        i++;
    }
    return arr;
}

//////

/////////// Dutch National Flag

void dutch_flag_sort(vector<char> &balls)
{
    int n = balls.size();

    int r = -1;
    int g = -1;
    int i = 0;

    while (i < n) // O(n)
    {
        if (balls[i] == 'G')
        {
            g++;
            swap(balls[g], balls[i]);
        }
        else if (balls[i] == 'R')
        {
            g++;
            swap(balls[g], balls[i]);

            r++;
            swap(balls[r], balls[g]);
        }
        i++;
    }
}

// O(n * (k-1)) -- O(n*k) for k-color

///////////

// Quick Sort

// lomuto partition
int partition(vector<int> &arr, int start, int end)
{
    int pivot = arr[start];
    int smaller = start;

    for (int i = start + 1; i <= end; i++)
    {
        if (arr[i] <= pivot)
        {
            smaller++;
            swap(arr[smaller], arr[i]);
        }
    }

    swap(arr[smaller], arr[start]);
    return smaller;
}

void helper(vector<int> &arr, int start, int end)
{
    if (start >= end)
        return;

    int random_index = rand() % (end - start) + start;
    swap(arr[random_index], arr[start]);

    int idx = partition(arr, start, end);

    helper(arr, start, idx - 1);
    helper(arr, idx + 1, end);
}

vector<int> quickSort(vector<int> &nums)
{
    int n = nums.size();
    helper(nums, 0, n - 1);
    return nums;
}

///////////////

// Hoare's - 1st version

vector<int> solve(vector<int> arr)
{

    int n = arr.size();

    int left = 0, right = n - 1;
    while (right > left)
    {
        if (arr[right] % 2 == 0)
        {
            swap(arr[left], arr[right]);
            left++;
        }
        else
        {
            right--;
        }
    }
    return arr;
}

/// 2nd variation

vector<int> solve(vector<int> arr)
{

    int n = arr.size();

    int left = 0, right = n - 1;
    // Move the pointers till they cross each other
    while (right > left)
    {
        if (arr[left] % 2 != 0)
        {
            swap(arr[left], arr[right]);
            right--;
        }
        else
        {
            left++;
        }
    }
    return arr;
}

// 3rd variation

vector<int> solve(vector<int> arr)
{
    int n = arr.size();
    int left = 0, right = n - 1; // i -- j
    while (right > left)         // i < j
    {
        while (left < right && arr[left] % 2 == 0) // red
        {
            left++; // i++
        }
        while (left < right && arr[right] % 2 != 0) // green
        {
            right--; // j--
        }

        swap(arr[left], arr[right]);
    }
    return arr;
}

// 4th Variation

vector<int> solve(vector<int> arr)
{

    int n = arr.size();

    int left = -1, right = n;
    // Move the pointers till they cross each other
    while (right - left > 1)
    {
        if (arr[left + 1] % 2 == 0)
        {
            left++;
        }
        else
        {
            right--;
            swap(arr[left + 1], arr[right]);
        }
    }
    return arr;
}

/////////// Dutch National Flag - Hoare's Partitioning

void dutch_flag_sort(vector<char> &balls)
{
    int n = balls.size();

    int r = 0;
    int g = 0;
    int b = n - 1;

    while (g <= b)
    {
        if (balls[g] == 'G')
        {
            g++;
        }
        else if (balls[g] == 'B')
        {
            swap(balls[g], balls[b]);
            b--;
        }
        else //  if (balls[g] == 'R')
        {
            swap(balls[g], balls[r]);
            g++;
            r++;
        }
    }
}

// Lumoto - k - k - 1 swaps hore's k - k-2 swaps

//I take TC Sessions - on Mon, Wed and Fri at 7 - 9 pm PT, every week

//  Discord - id : Shashi Bhusahn #6411
