#include<vector>
#include<string>
using namespace std;
namespace A1
{

    template < typename... T >
    int MaximumValue(T... values)
    {
        vector<T>valueList = {values ...};
        for(int i=0 ; i<valueList.size()-1 ; i++)
        {
            for(int j=i+1 ; j<valueList.size() ; j++)
            {
                if (valueList.get(i)<valueList.get(j))
                {
                    int a = valueList.get(i);
                    valueList.get(i) = valueList.get(j);
                    valueList.get(j) = a;
                }
            }
        }
        return valueList[0];
    }

    int main(int argc, char const *argv[])
    {
        return 0;
    }

    vector<int> CommonIntegerElements(int list1[], int list2[] , int len1 , int len2)
    {
        int n = 0 ;
        for(int i=0 ; i<len1 ; i++)
            for(int j=0 ; j<len2 ; j++)
                if (list1[i]==list2[j])
                    n = n + 1;

        vector<int> commonIntegerList; 

        for(int i=0 ; i<len1 ; i++)
        {
            for(int j=0 ; j<len2 ; j++)
            {
                if (i==list2[j])
                {
                    commonIntegerList[n-1] = i;
                    n = n - 1;
                }
            }
        }
        for(int i=0 ; i<n-1 ; i++)
        {
            if (commonIntegerList[i] > commonIntegerList[i+1])
            {
                int a = commonIntegerList[i];
                commonIntegerList[i] = commonIntegerList[i+1];
                commonIntegerList[i+1] = a;
            }
        }
        return commonIntegerList;
    }

    vector<string> CommonStringElements(string list1[], string list2[] , int len1 , int len2)
    {
        int n = 0 ;
        for(int i=0 ; i<len1 ; i++)
            for(int j=0 ; j<len2 ; j++)
                if (list1[i]==list2[j])
                    n = n + 1;

        vector<string> commonStringList ;

        for(int i=0 ; i<len1 ; i++)
        {
            for(int j=0 ; j<len2 ; j++)
            {
                if (list1[i]==list2[j])
                {
                    commonStringList[n-1] = i;
                    n = n - 1;
                }
            }
        }
        for(int i=0 ; i<n-1 ; i++)
        {
            for(int j=i+1 ; j<n ; j++)
            {
                if (commonStringList[j].compare(commonStringList[i])>0)
                {
                    string a = commonStringList[i];
                    commonStringList[i] = commonStringList[i+1];
                    commonStringList[i+1] = a;
                }
           }
        }
        return commonStringList;
    }

    // template < template typename _type>
    // _type* CommonElements <_type> (_type list1[], _type list2[] , int len1 , int len2)
    // {
    //     int n = 0 ;
    //     for( _type i : list1)
    //         for(int j=0 ; j<len2 ; j++)
    //             if (i.Equals(list2[j]))
    //                 n = n + 1;

    //         _type[] commonElementList = new  _type[n];
    //     n = 0;
    //     for( _type i : list1)
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
}