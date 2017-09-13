class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    n_splits = 3
    scores = []
    best_score, best_model = float("-inf"), None
    
    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        
        # Implement model selection using CV
        for n_components in range(self.min_n_components, self.max_n_components + 1):
            scores = []
            model, logL = None, None
            
            if(len(self.sequences) < n_splits):
                break

        folds = KFold(n_splits=n_splits, shuffle=True, random_state=self.random_state)
        for train_index, test_index in folds.split(self.sequence):
            X_train, lengths_train = combine_sequences(train_index, self.sequences)
            X_test, lengths_test = combine_sequences(test_index, self.sequences)
            try:
                model = GaussianHMM(n_components=self.num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(X_train, lengths_train)
                logL = model.score(X_test, lengths_test)
                scores.append(logL)
            except Exception as e:
                break
                
        logL_mean = np.mean(scores) if len(scores) > 0 else float("-inf")
        
        
        return 

