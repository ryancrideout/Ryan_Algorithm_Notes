'''
These are some notes on understanding the Principle Component Analysis step by step, using this as an example:

https://medium.com/analytics-vidhya/understanding-principle-component-analysis-pca-step-by-step-e7a4bb4031d9

Steps in general:
Step 1: Standardize the dataset.
Step 2: Calculate the covariance matrix for the features in the dataset.
Step 3: Calculate the eigenvalues and eigenvectors for the covariance matrix.
Step 4: Sort eigenvalues and their corresponding eigenvectors.
Step 5: Pick k eigenvalues and form a matrix of eigenvectors.
Step 6: Transform the original matrix.
'''

def step_1_standardize_the_dataset():
    # Assume we have this data set matrix.
    test_array = {
        "feature_1": [1, 5, 1, 5, 8],
        "feature_2": [2, 5, 4, 3, 1],
        "feature_3": [3, 6, 2, 2, 2],
        "feature_4": [4, 7, 3, 1, 2],
    }

    # The FIRST thing we need to do is standardize the data set, and to do that we need
    # to calculate the mean and standard deviation for each feature.

    def standarization_notes():
        '''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Mean and Standard Deviation Calculations
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        feature_1 mean: (1 + 5 + 1 + 5 + 8) / 5 = 4
        Standard Deviation formula: sqrt((Summation of (value - mean) ^ 2) / N)
        feature_1 standard deviation: 9 + 1 + 9 + 1 + 16 = 36, 36 / 4 = 9, sqrt(9) = 3
        And so on and so forth.

        (mean, standard deviation)
        feature_1 = (4, 3)
        feature_2 = (3, 1.58114)
        feature_3 = (3, 1.73205)
        feature_4 = (3.4, 2.30217)
        '''

        '''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Standardization Formula
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        standarized_value = (value - mean) / standard_deviation

        value = test_array["feature_1"][0] = 1

        standarized_value = (1 - 4) / 3 = -1
        '''

    # These are the standardized values:
    # Note for this new standardized matrix, the mean for each FEATURE is 0,
    # and the standard deviation is 1.
    test_array = {
        "feature_1": [-1, 0.33333, -1, 0.33333, 1.33333],
        "feature_2": [-0.63246, 1.26491, 0.63246, 0, -1.26491],
        "feature_3": [0, 1.73205, -0.57735, -0.57735, -0.57735],
        "feature_4": [0.26062, 1.56374, -0.17375, -1.04249, -0.60812],
    }


def step_2_calculate_covariance_matrix():
    def covariance_matrix_notes():
        '''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Calculating the Covariance Matrix
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        The covariance matrix will look something like this:
        [cov(f1,f1), cov(f1,f2), cov(f1,f3), cov(f1,f4)]
        [cov(f2,f1), cov(f2,f2), cov(f2,f3), cov(f2,f4)]
        [cov(f3,f1), cov(f3,f2), cov(f3,f3), cov(f3,f4)]
        [cov(f4,f1), cov(f4,f2), cov(f4,f3), cov(f4,f4)]

        Glossary:
        cov - covariance
        fX - feature_X

        With cov(x,y) being equal to:
        cov(x,y) = Summation of ((x_value - x_mean) * (y_value - y_mean)) / N elements

        So cov(f1,f1) is:
        cov(f1,f1) = ((-1-0)*(-1-0) + (0.33333-0)*(0.33333-0) + (-1-0)*(-1-0) + (0.33333-0)*(0.33333-0) + (1.33333-0)*(1.33333-0)) / 5
        cov(f1,f1) = 0.8

        And cov(f1,f2) is:
        cov(f1,f2) = ((-1-0)*(-0.63246-0) + (0.33333-0)*(0.1.26491-0) + (-1-0)*(0.63246-0) + (0.33333-0)*(0-0) + (1.33333-0)*(-1.26491-0)) / 5
        cov(f1,f2) = -0.25298
        '''

    # Our covariance matrix will look like this:
    covariance_matrix = [
        [0.8, -0.25298, 0.03849, -0.14479],
        [-0.25298, 0.8, 0.51121, 0.4945],
        [0.03849, 0.51121, 0.8, 0.75236],
        [-0.14479, 0.4945, 0.75236, 0.8],
    ]


def step_3_calculate_eigenvalues_and_eigenvectors():
    def eigenvalue_notes():
        '''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Calculating the Eigenvalues
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Let A be a square matrix (so in this case, our above covariance_matrix), v is a
        vector and λ a scalar that satisfies this equation:

        Av = λv

        If this holds true then λ is an eigenvalue associated with the eigenvector v.

        NOTE: A vector is a matrix with one column and a scalar is a real number to which
        you can multipy it to all values in a matrix. "I" is the identity matrix.

        Anyways we can rearrange the above formula as such:

        Av - λv = 0
        (A - λI)v = 0

        Since v is a non-zero vector, the only way the equation can be equal to zero is
        if the determinant of (A - λI) is also 0. The proof of this goes into linear
        algebra, which is beyond this exercise.

        Still, here's a proof:
        https://mathworld.wolfram.com/CramersRule.html
        https://mathworld.wolfram.com/Eigenvalue.html (And this is good for context)

        This explains determinants:
        https://www.mathsisfun.com/algebra/matrix-determinant.html

        NOTE: The determinant of (A - λI) can be written as det(A - λI)

        To calculate det(A - λI), we need to solve the following matrix for λ:

        det(A - λI) = [
            [0.8 - λ, -0.25298, 0.03849, -0.14479],
            [-0.25298, 0.8 - λ, 0.51121, 0.4945],
            [0.03849, 0.51121, 0.8 - λ, 0.75236],
            [-0.14479, 0.4945, 0.75236, 0.8 - λ],
        ]

        And solving for λ gives us the following eigenvalues:

        λ = 2.51579324, 1.0652885, 0.39388704, 0.02503121

        For an explanation on how to find the determinant of a matrix, go here:
        https://www.mathsisfun.com/algebra/matrix-determinant.html
        '''

    # Our eigenvalues are as follows:
    eigenvalue_1 = 2.51579324
    eigenvalue_2 = 1.0652885
    eigenvalue_3 = 0.39388704
    eigenvalue_4 = 0.02503121

    def eigenvector_notes():
        '''
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Calculating the Eigenvectors
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Now we solve the (A - λI)v = 0 equation using our different eigenvalues that we
        calculated.

        Consider (A - λI) again:

        (A - λI) = [
            [0.8 - λ, -0.25298, 0.03849, -0.14479],
            [-0.25298, 0.8 - λ, 0.51121, 0.4945],
            [0.03849, 0.51121, 0.8 - λ, 0.75236],
            [-0.14479, 0.4945, 0.75236, 0.8 - λ],
        ]

        And v is a vector that looks like this:
        v = [
            v_1,
            v_2,
            v_3,
            v_4,
        ]

        This is a good resource for finding out how to calculate eigenvectors:
        https://www.youtube.com/watch?v=IdsV0RaC9jM
        And this offers further explanation:
        https://www.mathsisfun.com/algebra/eigenvalue.html

        So for (A - λI)v = 0, we input different eigenvalues to get our different
        eigenvectors.

        So for λ = 2.51579324 (eigenvalue_1), we get the following values for one
        of our eigenvectors:

        eigenvector_1 = [
            0.16195986,
            -0.52404813,
            -0.58589647,
            -0.59654663,
        ]

        Using this same approach we can find the other eigenvectors from our eigenvalues, and then
        create a 4x4 matrix like so:

        eigenvectors = [
            [v1_1, v2_1, v3_1, v4_1],
            [v1_2, v2_2, v3_2, v4_2],
            [v1_3, v2_3, v3_3, v4_3],
            [v1_4, v2_4, v3_4, v4_4],
        ]
        '''

    # Our eigenvectors will look like this:
    eigenvectors = [
        [0.16195986, -0.917059, -0.307071, 0.196162],
        [-0.52404813, 0.206922, -0.817319, 0.120610],
        [-0.58589647, -0.320539, 0.188250, -0.720099],
        [-0.59654663, 0.115935, 0.449733, 0.654547],
    ]


def step_4_sort_eigenvalues_and_eigenvectors():
    # In our case the eigenvalues and eigenvectors are already sorted,
    # but it's common practice to sort by the largest eigenvalues to
    # the smallest.

    # There are also a lot of sorting algorithms to help with this.

    # NOTE: We sort by eigenvalues and then associate eigenvectors to
    # them.
    sorted = True


def step_5_pick_k_eigenvalues_make_eigenvector_matrix():
    # If we pick our top 2 eigenvectors, our matrix will look like this:

    top_2_eigenvectors = [
        [0.16195986, -0.917059],
        [-0.52404813, 0.206922],
        [-0.58589647, -0.320539],
        [-0.59654663, 0.115935],
    ]


def step_6_transform_the_original_matrix():
    # Consider our standardized feature matrix:
    feature_matrix = {
        "feature_1": [-1, 0.33333, -1, 0.33333, 1.33333],
        "feature_2": [-0.63246, 1.26491, 0.63246, 0, -1.26491],
        "feature_3": [0, 1.73205, -0.57735, -0.57735, -0.57735],
        "feature_4": [0.26062, 1.56374, -0.17375, -1.04249, -0.60812],
    }

    # Which if we reorganize to be consistent with our matrixes:
    feature_matrix = [
        [-1, -0.63246, 0, 0.26062],
        [0.33333, 1.26491, 1.73205, 1.56374],
        [-1,  0.63246, -0.57735, -0.17375],
        [0.33333, 0, -0.57735,  -1.04249],
        [1.33333, -1.26491, -0.57735, -0.60812],
    ]

    # And these are our top 2 eigenvectors:
    top_2_eigenvectors = [
        [0.16195986, -0.917059],
        [-0.52404813, 0.206922],
        [-0.58589647, -0.320539],
        [-0.59654663, 0.115935],
    ]

    # And if we do feature_matrix * top_2_eigenvectors, we get our transformed data:
    # feature_matrix * top_2_eigenvectors = transformed_data

    transformed_data = [
        [0.014003, 0.755975],
        [-2.556534, -0.780432],
        [-0.051480, 1.253135],
        [1.014150, 0.000239],
        [1.579861, -1.228917],
    ]

    # And that's it! We can compare our results to sklearn to verify that we did this correctly.