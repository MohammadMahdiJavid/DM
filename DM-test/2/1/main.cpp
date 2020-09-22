#include<iostream>
#include<vector>
#include<string>
using namespace std;

// template <typename _type>
// vector<_type> CommonElements (_type list1[], _type list2[] , int len1 , int len2)
// {
//     int n = 0 ;
//     for(auto i : list1)
//         for(int j=0 ; j<len2 ; j++)
//             if (i.Equals(list2[j]))
//                 n = n + 1;
//         _type[] commonElementList = new _type[n];
//     n = 0;
//     for(auto i : list1)
//     {
//         for(int j=0 ; j<len2 ; j++)
//         {
//             if (i.Equals(list2[j]))
//             {
//                 commonElementList[n] = i;
//                 n = n + 1;
//             }
//         }
//     }
//     return commonElementList;
// }

int test(int nums1[])
{
    for(auto i : nums1)
    {
        cout<<nums1;
    }
}
int main(int argc, char const *argv[])
{
    int nums2[] = {1, 2, 3};
    test(nums2);

    // string str1[] = {"Hello", "All", "Cpp", "Ap"}; 
    // string str2[] = { "Ap", "Programming", "First", "Language", "Microsoft", "All", "Cpp" }; 
    // vector<string> res=CommonElements(str1,str2,4,7);
    // vector<string> exp1{"All", "Cpp", "Ap"};
    // if( res == exp1 )
    //     cout<<"success";

    // int nums1[] = { 1, 54, 125, 23, 644, 31, 5, 61 }; 
    // int nums2[] = { 125, 23, 2, 3, 1001, 22, 5, 234, 31, 94 }; 
    // vector<int> num=CommonElements(nums1,nums2,8,10);
    // vector<int> exp2{125, 23, 31, 5};
    // if( num ==  exp2 )
    //     cout<<"SUCCESS";
    return 0;
}
