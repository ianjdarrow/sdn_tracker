<template>
  <div class="container" id="content">
  <div class="row">
    <div class="eight columns">
      <h2>SDN List Search <span v-if='loading'>(loading most recent)</span></h2>
      <h3 v-if='error'>Error retrieving data</h3>
    </div>
    <div id="logoContainer" class="four columns">
    <img id="logo" src="../../static/lx.png" alt="LedgerX">
    </div>
  </div>
  <div class="row">
    <div class="four columns">
      <input type='text' class="input" v-model="search" placeholder="Enter a name" :disabled="error || loading">
    </div>
    <div class="two columns">
      <input type='checkbox' id='indCheckbox' v-model='showIndividuals'>
      <label for='indCheckbox'>Individuals</label>  
    </div>
    <div class="two columns">
      <input type='checkbox' id='entityCheckbox' v-model='showEntities'>
      <label for='entityCheckbox'>Entities</label>
    </div>
  </div>
  <div v-if='!loading && isInput'>
    <div id="ind-table" v-if='showIndividuals'>
      <h4>Individuals: {{ filteredIndividuals.length }}</h4>
      <table class="twelve columns">
        <thead v-if='filteredIndividuals.length > 0'>
          <tr>
            <th class="name-column">Name</th>
            <th class="info-column">Details</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="individual in filteredIndividuals">
            <td>{{ individual.name }}</td>
            <td>{{ individual.details }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div id="entity-table" v-if='showEntities'>
      <h4>Entities: {{ filteredEntities.length }}</h4>
      <table class="twelve columns">
        <thead v-if='filteredEntities.length > 0'>
          <tr>
            <th class="name-column">Entity Name</th>
            <th class="info-column">Affiliation</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entity in filteredEntities">
            <td>{{ entity.name }}</td>
            <td>{{ entity.details }}</td>
          </tr>
        </tbody>
      </table>
      </div>
      <div class="row">
      </div>
    </div>
    <div class="twelve columns footer">
      <p>Made by <a href="mailto:ian@ledgerx.com">Ian</a> in 2017 (<a href="https://github.com/ianjdarrow/sdn_tracker">Github</a>)</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'index',
  data () {
    return {
      msg: 'LedgerX SDN Checker',
      sdnList: {
        individuals: [],
        entities: []
      },
      showIndividuals: true,
      showEntities: true,
      search: '',
      error: false,
      loading: true,
    }
  },
  methods: {
    getSDNList: function() {
      this.$http.get('http://127.0.0.1:5000/list').then(response => {
        this.sdnList.individuals = response.body.individuals;
        this.sdnList.entities = response.body.entities;
        this.loading = false;
        }, response => {
          this.error = true;
          this.loading = false;
        }
      );
    },
  },
  computed: {
    filteredIndividuals: function() {
      return this.sdnList.individuals.filter(individual => {
        return individual.name.indexOf(this.search.toUpperCase()) > -1
      });
    },
    filteredEntities: function() {
      return this.sdnList.entities.filter(entity => {
        return entity.name.indexOf(this.search.toUpperCase()) > -1
      });
    },
    isInput: function() {
      return (this.search.length > 1);
    },
  },
  created: function() {
    this.getSDNList();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

th, td {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tr {
  height: 25px;
  vertical-align: top;
  line-height: 1.35em;
}

label {
  display: inline-block;
}

#content {
  min-height: 90vh;
}

#logoContainer {
    height: 60px;  
    align-items: flex-end;
    display: flex;
    flex-direction: column;
}

#logo {
  margin-top: 10px;
  align-self: flex-end;
}

.input {
  width: 100%;
}

.results {

}

.name-column {
  width: 33%;
}

.info-column {
  width: 67%;
}

.footer {
  text-align: center;
  font-weight: lighter;
  color: #999;
  height:60px;
  position: absolute;
  bottom: 0;
  padding-top: 60px;
}


</style>
